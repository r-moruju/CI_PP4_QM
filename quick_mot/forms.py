
from allauth.account.forms import SignupForm
from django import forms
from bookings.models import Booking
from bootstrap_datepicker_plus.widgets import DatePickerInput


class CustomSignupForm(SignupForm):
    """
    An edited allauth SignupForm to get more user information
    like First an Last name
    """
    first_name = forms.CharField(max_length=30, min_length=3,
                                 label='First Name')
    last_name = forms.CharField(max_length=30, min_length=3,
                                label='Last Name')
    phone_number = forms.CharField(max_length=15, min_length=9,
                                   label='Phone Number')

    def save(self, request):
        user = super(CustomSignupForm, self).save(request)
        user.first_name = self.cleaned_data['first_name']
        user.last_name = self.cleaned_data['last_name']
        user.phone_number = self.cleaned_data['phone_number']
        user.save()
        return user


class BookingForm(forms.Form):
    """
    A form used to get Date input from the user
    Use django-bootstrap-datepicker-plus for a better UX
    """
    date = forms.DateField(widget=DatePickerInput(options={
        'format': "YYYY/MM/DD"
    }))


class ChangeBookingForm(forms.ModelForm):
    """
    A ModelForm based on Booking model,
    used to edit booking date
    """
    class Meta:
        model = Booking
        fields = ['date']
