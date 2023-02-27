from django.contrib import admin
from .models import Car, Booking, Site


@admin.register(Car)
class CarAdmin(admin.ModelAdmin):

    list_filter = ('booked', 'mot_expire_date')
    list_display = ('reg_number', 'owner', 'booked', 'make')
    search_fields = ('owner', 'reg_number')


@admin.register(Booking)
class BookingAdmin(admin.ModelAdmin):

    list_filter = ('date',)
    list_display = ('car', 'author', 'date')


@admin.register(Site)
class SiteAdmin(admin.ModelAdmin):

    list_display = ('header', )
