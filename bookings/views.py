from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from .models import Car, Booking
from quick_mot.forms import BookingForm, ChangeBookingForm
from quick_mot.mot_api import get_car_data


def home(request):
    if request.user.is_authenticated:
        bookings = Booking.objects.filter(author=request.user)
    else:
        bookings = None
    return render(request, '../templates/index.html', {'bookings': bookings})


def confirm_car(request):
    if request.user.is_authenticated:
        bookings = Booking.objects.filter(author=request.user)
    else:
        bookings = None
    data = request.session['data']
    context = {
        'data': data,
        'bookings': bookings
    }
    return render(request, "confirm_car.html", context)


def add_car_reg(request):
    if request.user.is_authenticated:
        bookings = Booking.objects.filter(author=request.user)
    else:
        bookings = None
    if request.method == "POST":
        field = request.POST.get('car_reg')
        car_data = get_car_data(field.upper())
        request.session['data'] = car_data
        return redirect('confirm_car')

    return render(request, 'add_car_reg.html', {'bookings': bookings})


def add_booking(request):
    if request.user.is_authenticated:
        bookings = Booking.objects.filter(author=request.user)
    else:
        bookings = None
    data = request.session['data']

    if not Car.objects.filter(reg_number=data['registrationNumber']).exists():
        car = Car(
            owner=request.user,
            make=data['make'],
            reg_number=data['registrationNumber'],
            mot_expire_date=data['motExpiryDate'],
            color=data['colour'],
            manufacturing_year=data['yearOfManufacture'],
            booked=False
        )
        car.save()

    form = BookingForm()
    context = {
        'form': form,
        'bookings': bookings
    }
    return render(request, 'add_booking.html', context)


def confirm_booking(request):
    data = request.session['data']
    current_car = Car.objects.filter(reg_number=data['registrationNumber'])[0]
    if request.method == "POST":
        input_field = request.POST.get('date')
        if current_car.booked is True:
            messages.warning(request,
                             'This car is allready booked!')
            return redirect('add_car_reg')
        else:
            current_car.booked = True
            current_car.save()
            booking = Booking(
                author=request.user,
                date=input_field,
                car=current_car
            )
            booking.save()
            messages.warning(request,
                             f'Successfully booked {current_car}')
            return redirect('home')


def delete_booking(request, booking_id):
    item = get_object_or_404(Booking, id=booking_id)
    item.delete()
    car = item.car
    car.booked = False
    car.save()
    return redirect("home")


def change_booking(request, booking_id):
    booking = get_object_or_404(Booking, id=booking_id)
    if request.method == "POST":
        form = ChangeBookingForm(request.POST, instance=booking)
        if form.is_valid():
            form.save()
            messages.warning(request,
                             'Booking date have been changed.')
            return redirect("home")
    form = ChangeBookingForm(instance=booking)
    context = {
        'booking': booking,
        'form': form
    }

    return render(request, 'change_booking.html', context)
