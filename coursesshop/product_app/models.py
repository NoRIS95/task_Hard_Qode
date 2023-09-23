from datetime import timedelta, datetime
from django.db import models
from datetime import datetime


class User(models.Model):
    user_id = models.IntegerField(blank=True, null=True)
    first_name = models.CharField(max_length=20)
    last_name = models.CharField(max_length=20)
    role = models.CharField(max_length=20)
    created_at = models.DateTimeField(default=datetime.now())

    def __str__(self) -> str:
        return self.last_name

    class Meta:
        verbose_name = "Пользователь"
        verbose_name_plural = "Пользователи"

class Product(models.Model):
    prod_id = models.IntegerField(blank=True, null=True)
    name  = models.CharField(max_length=20)
    owner_id = models.IntegerField(blank=True, null=True)
    # phone = models.CharField(max_length=20)
    # email = models.CharField(max_length=30)

    def __str__(self) -> str:
        return self.name

    class Meta:
        verbose_name = "Продукт"
        verbose_name_plural = "Продукты"

class WatchStatuses(models.Model):
    les_id = models.IntegerField(blank=True, null=True)
    user_id = models.IntegerField(blank=True, null=True)
    status = models.CharField(max_length=20)

    def __str__(self) -> str:
        return self.status


class Lesson(models.Model):
    les_id = models.IntegerField(blank=True, null=True)
    name  = models.CharField(max_length=20)
    video_link  = models.CharField(max_length=300)
    length_seconds = models.CharField(max_length=20)

    def __str__(self) -> str:
        return self.name

    class Meta:
        verbose_name = "Урок"
        verbose_name_plural = "Уроки"


class View(models.Model):
    les_id = models.IntegerField(blank=True, null=True)
    user_id = models.IntegerField(blank=True, null=True)
    date = models.DateTimeField()
    from_seconds = models.IntegerField(blank=True, null=True)
    to_seconds = models.IntegerField(blank=True, null=True)

    def __str__(self) -> str:
        return self.date


# class ProductsLessonsRelations(models.Model):
#     prod_id = models.ForeignKey(Product, on_delete = models.DO_NOTHING)
#     les_id = models.ForeignKey(Lesson, on_delete = models.DO_NOTHING)



























# class Hotel(models.Model):
#     name     = models.CharField(max_length=20)
#     location = models.CharField(max_length=50)
#     phone    = models.CharField(max_length=20)
#     email    = models.CharField(max_length=30)

#     def __str__(self) -> str:
#         return self.name


# class Room(models.Model):
#     room_no   = models.IntegerField(default=101)
#     price     = models.FloatField(default=1000.0)
#     hotel     = models.ForeignKey(Hotel, on_delete=models.CASCADE)
#     is_booked = models.BooleanField(default=False)

#     def __str__(self) -> str:
#         return str(self.room_no)

#     def hotel_name(self) -> str:
#         return self.hotel


# class Booking(models.Model):
#     guest         = models.ForeignKey(Guest, on_delete=models.CASCADE)
#     hotel         = models.ForeignKey(Hotel, on_delete=models.CASCADE)
#     room          = models.ForeignKey(Room, on_delete=models.CASCADE)
#     num_of_guest  = models.IntegerField(default=1)
#     checkin_date  = models.DateField(default=datetime.now)
#     checkout_date = models.DateField(default=datetime.now)
#     is_checkout   = models.BooleanField(default=False)

#     def __str__(self) -> str:
#         return self.guest.name

#     def hotel_name(self) -> str:
#         return self.hotel.hotel

#     def charge(self) -> float:
#         return self.is_checkout* \
#         (self.checkout_date - self.checkin_date + timedelta(1)).days* \
#         self.room.price