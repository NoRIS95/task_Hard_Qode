from django.urls import path
from .views import ProductStatisticsView, AccessibleProductsLessonsView, ProductLessonsView

urlpatterns = [
    path('accessible_lessons/', AccessibleProductsLessonsView.as_view(), name='accessible_lessons'),
    path('product_lessons/', ProductLessonsView.as_view(), name='product_lessons'),
    path('product_statistics/', ProductStatisticsView.as_view(), name='product_statistics'),
]