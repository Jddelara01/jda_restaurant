from django.db import models
from django.contrib.auth.models import User
from cloudinary.models import CloudinaryField
from phonenumber_field.modelfields import PhoneNumberField


# Table Model
class Table(models.Model):
    table_num = models.IntegerField(null=False, unique=True)
    max_capacity = models.IntegerField(null=False)


# Booking Model
class Booking(models.Model):
    fullname = models.CharField(max_length=55, unique=True)
    email = models.EmailField(max_length=55)
    phone = PhoneNumberField(unique=True, region='IE')
    date = models.DateField()
    time = models.TimeField()
    num_of_people = models.IntegerField(null=False)
    table_num = models.ForeignKey(Table, on_delete=models.CASCADE, related_name='bookings')  # noqa

    def __str__(self):
        return self.fullname
