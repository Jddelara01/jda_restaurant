from django import forms
from .models import Booking


class BookingForm(forms.ModelForm):

    class Meta:
        model = Booking

        fields = [
            'fullname',
            'email',
            'phone',
            'date',
            'time',
            'num_of_people',
            'table_num'
        ]
