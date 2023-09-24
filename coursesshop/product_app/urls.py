# from django.urls import re_path
# from .views import ListView


# urlpatterns = [
#     re_path(r"^(?P<api_name>[a-z]+)", ListView, name='product-objects'),
# ]

from django.urls import path, re_path
from .views import AccessibleProductsLessonsView, ProductLessonsView, ListView

urlpatterns = [
    re_path(r"^(?P<api_name>[a-z]+)", ListView, name='product-objects'),
    path('accessible_lessons/', AccessibleProductsLessonsView.as_view(), name='accessible_lessons'),
    path('product_lessons/<int:product_id>/', ProductLessonsView.as_view(), name='product_lessons'),
]

    # path('product_statistics/', ProductStatisticsView.as_view(), name='product_statistics'),