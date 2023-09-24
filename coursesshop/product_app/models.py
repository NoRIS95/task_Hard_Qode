from django.db import models
from django.contrib.auth.models import User


class Product(models.Model):
    name = models.CharField(max_length=200)
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    users_with_access = models.ManyToManyField(User, related_name='accessible_products', blank=True)


class Lesson(models.Model):
    title = models.CharField(max_length=200)
    video_url = models.URLField()
    duration_seconds = models.PositiveIntegerField()  # In seconds
    products = models.ManyToManyField(Product, related_name='lessons')


class LessonView(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    lesson = models.ForeignKey(Lesson, on_delete=models.CASCADE)
    date = models.DateTimeField(auto_now=True)
    view_time_seconds = models.PositiveIntegerField(default=0)


























