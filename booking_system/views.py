from django.shortcuts import render, get_object_or_404
from django.views import generic, View
from .models import Booking
from django.http import HttpResponse


class BookingDetail(View):

    def get(self, request, *args, **kw):
        queryset = Booking.objects
        booking = get_object_or_404(queryset)

        return render(request, 'booking.html', {
            "booking": booking
        },)
