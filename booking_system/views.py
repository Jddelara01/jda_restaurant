from django.shortcuts import render
from django.views import generic, View
from .models import Booking


class BookingDetail(View):

    def get(self, request):
        return render(request, 'booking.html')
