from django.db import models
from django.contrib.auth.models import User
from django.db.models import Avg


class Car(models.Model):
    """
    Model to store Car information
    """
    owner = models.ForeignKey(User, on_delete=models.CASCADE,
                              related_name='cars')
    reg_number = models.CharField(max_length=10, blank=False, null=False,
                                  unique=True)
    mot_expire_date = models.DateField()
    make = models.TextField()
    color = models.TextField()
    manufacturing_year = models.TextField()
    booked = models.BooleanField()

    def __str__(self) -> str:
        return f"{self.color} {self.make} from {self.manufacturing_year}"


class Booking(models.Model):
    """
    Model to store Booking information for specific Car and User
    """
    car = models.ForeignKey(Car, on_delete=models.CASCADE,
                            related_name="booking")
    author = models.ForeignKey(User, on_delete=models.CASCADE,
                               related_name='bookings')
    date = models.DateField(blank=False, null=False)
    created_on = models.DateTimeField(auto_now=True)

    def __str__(self) -> str:
        return f"{self.car} on {self.date}"


class Site(models.Model):
    """
    Simple model to store Site Rating Average
    Inspired from https://medium.com/geekculture/django-implementing-star-rating-e1deff03bb1c
    """
    header = models.CharField(max_length=100, default="Service Rating")

    def average_rating(self) -> float:
        return Rating.objects.filter(site=self).aggregate(Avg("rating"))["rating__avg"] or 0

    def __str__(self):
        return f"{self.header}: {self.average_rating()}"


class Rating(models.Model):
    """
    To store User ratig    
    Inspired from https://medium.com/geekculture/django-implementing-star-rating-e1deff03bb1c
    """
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    site = models.ForeignKey(Site, on_delete=models.CASCADE)
    rating = models.IntegerField(default=0)

    def __str__(self):
        return f"{self.site.header}: {self.rating}"
