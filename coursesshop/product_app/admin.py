from django.contrib import admin

from .models import Product, Lesson, User, View


admin.site.register(Product)
admin.site.register(Lesson)
admin.site.register(User)
# admin.site.register(WatchStatuses)
admin.site.register(View)