from django.shortcuts import render, redirect
from quick_mot.forms import CarsForm


def home(request):
    return render(request, '../templates/index.html')


def add_car_reg(request):
    if request.method == "POST":
        form = CarsForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("confirm_car")

    form = CarsForm
    context = {
        'form': form
    }
    return render(request, 'add_car_reg.html', context)
