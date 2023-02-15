from django.db import models
from django.contrib.auth.models import User


class Car(models.Model):
    owner = models.ForeignKey(User, on_delete=models.CASCADE,
                              related_name='cars')
    reg_number = models.CharField(max_length=10, blank=False, null=False,
                                  unique=True)
    mot_expire_date = models.DateField()
    make = models.TextField()
    color = models.TextField()
    manufacturing_year = models.TextField()
    booked = models.BooleanField(default=False)

    def __str__(self) -> str:
        return f"{self.color} {self.make} from {self.manufacturing_year}"


class Booking(models.Model):
    car = models.ForeignKey(Car, on_delete=models.CASCADE,
                            related_name="booking")
    author = models.ForeignKey(User, on_delete=models.CASCADE,
                               related_name='bookings')
    date = models.DateField(blank=False, null=False)
    created_on = models.DateTimeField(auto_now=True)

    def __str__(self) -> str:
        return f"{self.car} on {self.date}"
