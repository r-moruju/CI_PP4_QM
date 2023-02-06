
from allauth.account.forms import SignupForm
from django import forms
from bookings.models import Booking
from bootstrap_datepicker_plus.widgets import DateTimePickerInput


class CustomSignupForm(SignupForm):
    first_name = forms.CharField(max_length=30, label='First Name')
    last_name = forms.CharField(max_length=30, label='Last Name')
    phone_number = forms.CharField(max_length=15, label='Phone Number')

    def save(self, request):
        user = super(CustomSignupForm, self).save(request)
        user.first_name = self.cleaned_data['first_name']
        user.last_name = self.cleaned_data['last_name']
        user.phone_number = self.cleaned_data['phone_number']
        user.save()
        return user


class BookingForm(forms.ModelForm):
    class Meta:
        model = Booking
        fields = ['date']
        widgets = {'date': DateTimePickerInput(options={
            'format': "MM/DD/YYYY HH:mm"
        })}
