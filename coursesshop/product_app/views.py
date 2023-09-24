from rest_framework import  status
from rest_framework import generics
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework.views import APIView
from .models import Product, Lesson, User, View
from .serializer import ProductSerializer, LessonSerializer, UserSerializer,  ViewSerializer
from collections import namedtuple




nt = namedtuple("object", ["model", "serializers"])
pattern = {
    "product"  : nt(Product, ProductSerializer),
    "lesson"  : nt(Lesson, LessonSerializer),
    "user"  : nt(User, UserSerializer),
    "view"  : nt(View, ViewSerializer),
}


@api_view(["GET", "POST"])
def ListView(request, api_name):
    object =  pattern.get(api_name, None)
    if object == None:
        return Response(
            data   = "Invalid URL",
            status = status.HTTP_404_NOT_FOUND,
        )
    if request.method == "GET":
        object_list = object.model.objects.all()
        serializers  = object.serializers(object_list, many=True)
        return Response(serializers.data)

    if request.method == "POST":
        data = request.data
        serializers = object.serializers(data=data)
        
        if not serializers.is_valid():
            return Response(
                data   = serializers.error,
                status = status.HTTP_404_NOT_FOUND
            )
        serializers.save()
        return Response(
                data   = serializers.error,
                status = status.HTTP_201_CREATED
        )





#     "watch_statuses"  : nt(WatchStatuses, WatchStatusesSerializer),

class AccessibleProductsLessonsView(generics.ListAPIView):
    serializer_class = ProductSerializer

    def get_queryset(self):
        return self.request.user.accessible_products.all()

class ProductLessonsView(generics.RetrieveAPIView):
    serializer_class = ProductSerializer
    lookup_url_kwarg = 'product_id'
    queryset = Product.objects.all()

# class ProductStatisticsView(generics.ListAPIView):
#     """
#     Implement statistics view (define serializer and logic for getting statistics)
#     """
#     pass







# nt = namedtuple("object", ["model", "serializers"])
# pattern = {
#     "product"  : nt(Product, ProductSerializer),
#     "lesson"  : nt(Lesson, LessonSerializer),
#     "user"  : nt(User, UserSerializer),
#     "watch_statuses"  : nt(WatchStatuses, WatchStatusesSerializer),
#     "view"  : nt(View, ViewSerializer),
# }


# # class LesView(APIView):
# #     def get(self, request, les_id):
# #         lesson = Lesson.objects.get(id=les_id)
# #         lesson.views_count += 1
# #         lesson.save()
# #         serializer = LessonSerializer(lesson)
# #         return Response(serializer.data)




# @api_view(["GET", "POST"])
# def ListView(request, api_name):
#     object =  pattern.get(api_name, None)
#     if object == None:
#         return Response(
#             data   = "Invalid URL",
#             status = status.HTTP_404_NOT_FOUND,
#         )
#     if request.method == "GET":
#         object_list = object.model.objects.all()
#         serializers  = object.serializers(object_list, many=True)
#         return Response(serializers.data)

#     if request.method == "POST":
#         data = request.data
#         serializers = object.serializers(data=data)
        
#         if not serializers.is_valid():
#             return Response(
#                 data   = serializers.error,
#                 status = status.HTTP_404_NOT_FOUND
#             )
#         serializers.save()
#         return Response(
#                 data   = serializers.error,
#                 status = status.HTTP_201_CREATED
#         )