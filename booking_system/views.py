from django.shortcuts import render, HttpResponse, get_object_or_404, redirect
from django.views import generic, View
from .models import Booking, Table
from .forms import BookingForm
import warnings


def open_home_page(request):
    return render(request, 'index.html')


def make_reservation(request):

    booking_form = BookingForm(request.POST)
    if booking_form.is_valid():
        booking_form.save()

    return render(request, 'booking.html', {
        "booking_form": BookingForm()
    })


def get_reservation_detail(request):

    bookings = Booking.objects.all()

    return render(request, "display_booking.html", {
        'bookings': bookings
    })


def change_booking(request, booking_id):
    booking = get_object_or_404(Booking, id=booking_id)
    if request.method == 'POST':
        booking_form = BookingForm(request.POST, instance=booking)
        if booking_form.is_valid():
            booking_form.save()
            return redirect('get_reservation_detail')

    booking_form = BookingForm(instance=booking)
    context = {
        'booking_form': booking_form
    }
    return render(request, 'change_booking.html', context)


def delete_booking(request, booking_id):
    booking = get_object_or_404(Booking, id=booking_id)
    booking.delete()
    return redirect("get_reservation_detail")
