from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from .models import Car, Booking
from quick_mot.forms import BookingForm
from quick_mot.mot_api import get_car_data


def home(request):
    return render(request, '../templates/index.html')


def confirm_car(request):
    data = request.session['data']
    return render(request, "confirm_car.html", {'data': data})


def add_car_reg(request):
    if request.method == "POST":
        field = request.POST.get('car_reg')
        car_data = get_car_data(field.upper())
        request.session['data'] = car_data
        return redirect('confirm_car')

    return render(request, 'add_car_reg.html')


def add_booking(request):
    data = request.session['data']

    if not Car.objects.filter(reg_number=data['registrationNumber']).exists():
        car = Car(
            owner=request.user,
            make=data['make'],
            reg_number=data['registrationNumber'],
            mot_expire_date=data['motExpiryDate'],
            color=data['colour'],
            manufacturing_year=data['yearOfManufacture']
        )
        car.save()

    cars = Car.objects.all
    form = BookingForm()
    context = {
        'form': form,
        'cars': cars
    }
    return render(request, 'add_booking.html', context)


def confirm_booking(request):
    current_car = Car.objects.filter(owner=request.user)[0]
    if request.method == "POST":
        input_field = request.POST.get('date')
        if not current_car.booked:
            current_car.booked = True
            booking = Booking(
                author=request.user,
                date=input_field,
                car=current_car
            )
            booking.save()
            return redirect('home')
        else:
            messages.warning(request,
                             'This car is allready booked')
            return redirect('add_car_reg')
