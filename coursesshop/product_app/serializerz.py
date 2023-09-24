from rest_framework import serializers
from .models import Product, Lesson, LessonView
from .config import VIEW_FRACTION_THRESH

class LessonSerializer(serializers.ModelSerializer):
    status = serializers.SerializerMethodField()
    last_viewed = serializers.SerializerMethodField()
    view_time_seconds = serializers.SerializerMethodField()

    class Meta:
        model = Lesson
        fields = ['title', 'duration_seconds', 'id', 'status', 'last_viewed', 'view_time_seconds']

    def get_view_time_seconds(self, obj):
        lesson_views = obj.lessonview_set
        if 'user_id' in self.context:
            lesson_views = lesson_views.filter(user=self.context['user_id'])
        lesson_views = lesson_views.all()
        if len(lesson_views) == 0:
            return
        view_time_seconds = sum([x.view_time_seconds for x in lesson_views])
        return view_time_seconds

    def get_status(self, obj):
        lesson_views = obj.lessonview_set
        if 'user_id' in self.context:
            lesson_views = lesson_views.filter(user=self.context['user_id'])
        lesson_views = lesson_views.all()
        if len(lesson_views) == 0:
            return
        viewed = sum([x.view_time_seconds for x in lesson_views])/obj.duration_seconds>VIEW_FRACTION_THRESH
        return 'Viewed' if viewed else 'Not viewed'

    def get_last_viewed(self, obj):
        lesson_views = obj.lessonview_set
        if 'user_id' in self.context:
            lesson_views = lesson_views.filter(user=self.context['user_id'])
        lesson_views = lesson_views.all()
        if len(lesson_views) == 0:
            return
        return max([x.date for x in lesson_views])

class ProductSerializer(serializers.ModelSerializer):
    lessons = serializers.SerializerMethodField()

    class Meta:
        model = Product
        fields = ['name', 'lessons']

    def get_lessons(self, obj):
        return LessonSerializer(obj.lessons, many=True, context=self.context).data



class ProductStatisticsSerializer(serializers.ModelSerializer):
    number_of_lessons_viewed = serializers.IntegerField()
    total_view_time = serializers.IntegerField()
    number_of_students = serializers.IntegerField()
    product_purchase_percentage = serializers.FloatField()

    class Meta:
        model = Product
        fields = [
            'id',
            'name',
            'number_of_lessons_viewed',
            'total_view_time',
            'number_of_students',
            'product_purchase_percentage',
        ]