from rest_framework import fields, serializers
from .models import Product, Lesson, User, View


class LessonSerializer(serializers.HyperlinkedModelSerializer):
    # lesson_views = serializers.SerializerMethodField()
    class Meta:
        model  = Lesson
        fields = ("les_id", "name", "video_link", "length_seconds", "views_count", "products")
    def get_lesson_views(self, obj):
        lesson_views = obj.lessonview_set.filter(user=self.context['request'].user)
        return LessonViewSerializer(lesson_views, many=True).data

class ProductSerializer(serializers.HyperlinkedModelSerializer):
    # lessons = LessonSerializer(many=True)
    class Meta:
        model  = Product
        fields = ("prod_id", "name", "user_id")

class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model  = User
        fields = ("user_id", "first_name", "last_name", "role", "created_at")

# class WatchStatusesSerializer(serializers.HyperlinkedModelSerializer):
#     class Meta:
#         model  = WatchStatuses
#         fields = ("les_id", "user_id", "status")

class ViewSerializer(serializers.HyperlinkedModelSerializer):
    # status = serializers.SerializerMethodField()
    class Meta:
        model  = View
        fields = ("les_id", "user_id", "date", "from_seconds", "to_seconds")
    def get_status(self, obj):
        return 'Viewed' if obj.viewed else 'Not viewed'



# class ProductSerializer(serializers.HyperlinkedModelSerializer):
#     class Meta:
#         model  = Product
#         fields = ("prod_id", "name")


# class LessonSerializer(serializers.HyperlinkedModelSerializer):
#     class Meta:
#         model  = Lesson
#         fields = ("les_id", "name", "video_link", "lesson_views", "views_count")


# class UserSerializer(serializers.HyperlinkedModelSerializer):
#     class Meta:
#         model  = User
#         fields = ("user_id", "first_name", "last_name", "role", "created_at")


# class WatchStatusesSerializer(serializers.HyperlinkedModelSerializer):
#     class Meta:
#         model  = WatchStatuses
#         fields = ("les_id", "user_id", "status")



# # class ViewSerializer(serializers.ModelSerializer):
# #     status = serializers.SerializerMethodField()

# #     class Meta:
# #         model = LessonView
# #         fields = ['les_id', 'view_time', 'status', 'last_viewed']

# #     def get_status(self, obj):
# #         return 'Viewed' if obj.viewed else 'Not viewed'


# class ViewSerializer(serializers.HyperlinkedModelSerializer):
#     class Meta:
#         model  = View
#         fields = ['les_id', 'view_time', 'status', 'last_viewed']


#         # fields = ("les_id", "user_id", "view_date", "from_seconds", "to_seconds")

# # class ProductsLessonsRelationsSerializer(serializers.HyperlinkedModelSerializer):
# #     class Meta:
# #         model  = ProductsLessonsRelations
# #         fields = ("prod_id ", "les_id")

