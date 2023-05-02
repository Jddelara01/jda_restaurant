from django import forms
from .models import Booking
import datetime


class BookingForm(forms.ModelForm):

    class Meta:
        model = Booking

        fields = [
            'fullname',
            'email',
            'phone',
            'date',
            'time',
            'num_of_people'
        ]
