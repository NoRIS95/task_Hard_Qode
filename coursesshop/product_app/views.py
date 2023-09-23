from rest_framework import  status
from rest_framework.response import Response
from rest_framework.decorators import api_view

from .models import Product, Lesson, User, WatchStatuses, View
from .serializer import ProductSerializer, LessonSerializer, UserSerializer, WatchStatusesSerializer, ViewSerializer

from collections import namedtuple

nt = namedtuple("object", ["model", "serializers"])
pattern = {
    "product"  : nt(Product, ProductSerializer),
    "lesson"  : nt(Lesson, LessonSerializer),
    "user"  : nt(User, UserSerializer),
    "watch_statuses"  : nt(WatchStatuses, WatchStatusesSerializer),
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