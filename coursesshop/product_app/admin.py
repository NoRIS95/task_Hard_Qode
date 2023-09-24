from django.contrib import admin

from .models import Product, Lesson, LessonView
from django.contrib.auth.models import User


admin.site.register(Product)
admin.site.register(Lesson)
admin.site.register(LessonView)