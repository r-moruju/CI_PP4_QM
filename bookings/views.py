from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from .models import Car, Booking, Site, Rating
from quick_mot.forms import BookingForm, ChangeBookingForm
from quick_mot.mot_api import get_car_data


def home(request):
    """
    Render home page
    """
    if request.user.is_authenticated:
        bookings = Booking.objects.filter(author=request.user)
    else:
        bookings = None

    # Get current rating
    sites = Site.objects.all()
    for site in sites:
        if request.user.is_authenticated:
            rating = Rating.objects.filter(site=site,
                                           user=request.user).first()
        else:
            rating = 0
        site.user_rating = rating.rating if rating else 0
    return render(request, '../templates/index.html',
                  {'bookings': bookings, 'sites': sites})


def rate(request, site_id, rating):
    """
    Save new user rating
    """
    site = Site.objects.get(id=site_id)
    Rating.objects.filter(site=site, user=request.user).delete()
    site.rating_set.create(user=request.user, rating=rating)
    return redirect('home')


def confirm_car(request):
    """
    Display Car information for user to confirm
    """
    sites = Site.objects.all()
    if request.user.is_authenticated:
        bookings = Booking.objects.filter(author=request.user)
    else:
        bookings = None
    data = request.session['data']
    context = {
        'data': data,
        'bookings': bookings,
        'sites': sites
    }
    return render(request, "confirm_car.html", context)


def add_car_reg(request):
    """
    Get Car reg from the user
    Get API data
    """
    sites = Site.objects.all()
    if request.user.is_authenticated:
        bookings = Booking.objects.filter(author=request.user)
    else:
        bookings = None
    if request.method == "POST":
        field = request.POST.get('car_reg')
        car_data = get_car_data(field.upper())
        # Verify that the API returns usable data
        try:
            car_data['registrationNumber']
        except KeyError:
            messages.warning(request, 'Vehicle Not Found')
        else:
            request.session['data'] = car_data
            return redirect('confirm_car')
    return render(request, 'add_car_reg.html',
                  {'bookings': bookings, 'sites': sites})


def add_booking(request):
    """
    Save Car object
    """
    sites = Site.objects.all()
    if request.user.is_authenticated:
        bookings = Booking.objects.filter(author=request.user)
    else:
        bookings = None
    data = request.session['data']

    # Check if Car exists in database before save
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
        'bookings': bookings,
        'sites': sites
    }
    return render(request, 'add_booking.html', context)


def confirm_booking(request):
    """
    Create Booking object
    """
    data = request.session['data']
    current_car = Car.objects.filter(reg_number=data['registrationNumber'])[0]
    if request.method == "POST":
        input_field = request.POST.get('date')
        # Check if Car is booked
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
    """
    Delete Booking object
    """
    item = get_object_or_404(Booking, id=booking_id)
    item.delete()
    car = item.car
    car.booked = False
    car.save()
    messages.warning(request,
                     f'Booking deleted for {car}!')
    return redirect("home")


def change_booking(request, booking_id):
    """
    Change Booking date
    """
    sites = Site.objects.all()
    if request.user.is_authenticated:
        bookings = Booking.objects.filter(author=request.user)
    else:
        bookings = None
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
        'bookings': bookings,
        'booking': booking,
        'form': form,
        'sites': sites
    }
    return render(request, 'change_booking.html', context)
