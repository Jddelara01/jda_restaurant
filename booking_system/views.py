from django.shortcuts import render, get_object_or_404
from django.views import generic, View
from .models import Booking, Table
from django.http import HttpResponse
from .forms import BookingForm
import warnings


class BookingDetail(View):

    def get(self, request, *args, **kw):
        queryset = Booking.objects
        booking = get_object_or_404(queryset)

        return render(request, 'booking.html', {
            "booking": booking,
            "booking_form": BookingForm()
        },)

    def post(self, request, *args, **kw):
        queryset = Booking.objects
        queryset1 = Table.objects.filter(table_num=1)
        booking = get_object_or_404(queryset)
        table = get_object_or_404(queryset1)

        booking_form = BookingForm(data=request.POST)
        if booking_form.is_valid():
            # booking_form.save(commit=False)
            booking_form.instance.table_num = table
            booking_form.save()
            return render(request, 'booking.html', {
                "booking": booking,
                "booking_form": BookingForm()
            })
        else:
            return render(request, "index.html")
