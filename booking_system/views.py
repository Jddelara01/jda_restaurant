from django.shortcuts import render, get_object_or_404
from django.views import generic, View
from .models import Booking
from django.http import HttpResponse
from .forms import BookingForm


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
        booking = get_object_or_404(queryset)

        booking_form = BookingForm(data=request.POST)
        booking_form.save()

        return render(request, 'booking.html', {
            "booking": booking,
            "booking_form": BookingForm()
        },)
