from rest_framework import generics
from .models import Product, Lesson, LessonView
from django.contrib.auth.models import User
from .serializerz import ProductStatisticsSerializer, ProductSerializer
from django.db import models
from django.db.models import Count, Sum, F, FloatField, Subquery, OuterRef
from django.db.models.functions import Coalesce
from .config import VIEW_FRACTION_THRESH


class AccessibleProductsLessonsView(generics.ListAPIView):
    serializer_class = ProductSerializer
    
    def get_queryset(self):
        if user_id := self.request.GET.get('user_id'):
            user_id = int(user_id)
        users = User.objects.filter(id=user_id).all()
        if len(users) == 0: return
        user = users[0]
        products = user.accessible_products
        return products.all()

    def get_serializer_context(self):
        if user_id := self.request.GET.get('user_id'):
            user_id = int(user_id)
        context = super().get_serializer_context()
        context.update({"user_id": user_id})
        return context


class ProductLessonsView(AccessibleProductsLessonsView):
    def get_queryset(self):
        if product_id := self.request.GET.get('product_id'):
            product_id = int(product_id)
        return super().get_queryset().filter(id=product_id)

    def get_serializer_context(self):
        if product_id := self.request.GET.get('product_id'):
            product_id = int(product_id)
        context = super().get_serializer_context()
        context.update({"product_id": product_id})
        return context


class ProductStatisticsView(generics.ListAPIView):
    serializer_class = ProductStatisticsSerializer
    views = Lesson.objects.select_related('lessonview').values('products', 'id', 'lessonview__user')\
        .annotate(watched_fraction=Sum('lessonview__view_time_seconds')*1./Coalesce('duration_seconds', 0)).filter(watched_fraction__gt=VIEW_FRACTION_THRESH)
    
    users = User.objects
    try:
        users_count = users.count()
    except:
        users_count = 1
    queryset = Product.objects.annotate(
        number_of_lessons_viewed=Count(Subquery(views.filter(products=OuterRef('id')).values('id')), distinct=True),
        total_view_time=Coalesce(Sum('lessons__lessonview__view_time_seconds', distinct=True), 0),
        number_of_students=Count('users_with_access', distinct=True),
    ).annotate(
        product_purchase_percentage=(F('number_of_students') * 100 / users_count),
    )