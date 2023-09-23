from rest_framework import fields, serializers
from .models import Product, Lesson, User, WatchStatuses, View


class ProductSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model  = Product
        fields = ("prod_id", "name")

class LessonSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model  = Lesson
        fields = ("les_id", "name", "video_link", "length_seconds")

class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model  = User
        fields = ("user_id", "first_name", "last_name", "role", "created_at")

class WatchStatusesSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model  = WatchStatuses
        fields = ("les_id", "user_id", "status")

class ViewSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model  = View
        fields = ("les_id", "user_id", "date", "from_seconds", "to_seconds")

# class ProductsLessonsRelationsSerializer(serializers.HyperlinkedModelSerializer):
#     class Meta:
#         model  = ProductsLessonsRelations
#         fields = ("prod_id ", "les_id")


# class HotelSerializer(serializers.ModelSerializer):
#     class Meta:
#         model  = Hotel
#         fields = ("name", "location", "phone", "email")


# class RoomSerializer(serializers.ModelSerializer):
#     class Meta:
#         model  = Room
#         fields = ("room_no", "price", "hotel", "is_booked")


# class BookingSerializer(serializers.ModelSerializer):
#     guest = GuestSerializer
#     hotel = HotelSerializer
#     room  = RoomSerializer
#     class Meta:
#         model  = Booking
#         fields =("guest", "hotel", "room", "checkin_date", "checkout_date", "charge",)