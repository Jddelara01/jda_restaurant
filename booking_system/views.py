from django.shortcuts import render, get_object_or_404
from django.views import generic, View
from .models import Booking, Table
from django.http import HttpResponse
from .forms import BookingForm
import warnings


class BookingDetail(View):

    def get(self, request, *args, **kw):
        booking_query = Booking.objects.filter(email='jane@test.com')
        booking = get_object_or_404(booking_query)

        return render(request, 'booking.html', {
            "booking": booking,
            "booking_form": BookingForm()
        },)

    def post(self, request, *args, **kw):
        booking_query = Booking.objects.filter(email='jane@test.com')
        booking = get_object_or_404(booking_query)

        booking_form = BookingForm(data=request.POST)
        if booking_form.is_valid():
            booking_form.save(commit=False)
            if booking_form.cleaned_data['num_of_people'] == 4:
                table_query = Table.objects.filter(table_num=1)
                table = get_object_or_404(table_query)
                booking_form.instance.table_num = table
            else:
                table_query1 = Table.objects.filter(table_num=2)
                table1 = get_object_or_404(table_query1)
                booking_form.instance.table_num = table1
            booking_form.save()

            return render(request, 'booking.html', {
                "booking": booking,
                "booking_form": BookingForm()
            })
        else:
            return render(request, "index.html")
