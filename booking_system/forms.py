from django import forms
from .models import Booking
import datetime


class BookingForm(forms.ModelForm):

    class Meta:
        model = Booking

        fields = [
            'name',
            'email',
            'phone',
            'date',
            'time',
            'num_of_people'
        ]

        widgets = {
            'date': forms.SelectDateWidget(
                years=(
                    datetime.date.today().year, datetime.date.today().year + 1
                    )
                )
        }

        def __init__(self, *args, **kwargs):
            AVAILABLE_TIMES = ["17:30", "18:00", "18:30", "19:00", "19:30", "20:00"]  # noqa

            super(BookingForm, self).__init__(*args, **kwargs)
            self.fields['time'].widget = forms.Select(choices=AVAILABLE_TIMES)
