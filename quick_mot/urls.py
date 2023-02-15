"""quick_mot URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from bookings import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name='home'),
    path('accounts/', include('allauth.urls')),
    path('ad_car_reg/', views.add_car_reg, name='add_car_reg'),
    path('confirm_car/', views.confirm_car, name='confirm_car'),
    path('add_booking/', views.add_booking, name='add_booking'),
    path('add_booking/confirm_booking', views.confirm_booking, name='confirm_booking'),
    path('delete_booking/<booking_id>', views.delete_booking, name='delete_booking')
]
