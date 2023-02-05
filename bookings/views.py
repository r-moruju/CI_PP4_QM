from django.shortcuts import render, redirect, get_object_or_404
from .models import Car
# from quick_mot.forms import CarsForm
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