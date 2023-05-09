from django.db import models
from django.contrib.auth.models import User
from cloudinary.models import CloudinaryField
from phonenumber_field.modelfields import PhoneNumberField
from django.core.validators import MinValueValidator, MaxValueValidator


# Table Model
class Table(models.Model):
    """
    These will be the tables that can be assigned to a booking that will
    depend on the capacity of the table and the number of people per booking
    """
    capacity = models.PositiveIntegerField(default=1)

    def __str__(self):
        return str(self.pk)


# Booking Model
class Booking(models.Model):
    fullname = models.CharField(max_length=55, unique=True)
    email = models.EmailField(max_length=55)
    phone = PhoneNumberField(unique=True, region='IE')
    date = models.DateField()
    time = models.TimeField()
    num_of_people = models.IntegerField(
        validators=[
            MaxValueValidator(8),
            MinValueValidator(1)
        ]
    )
    table_num = models.ManyToManyField(Table)

    def __str__(self):
        return self.fullname
