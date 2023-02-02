from django.db import models
from django.contrib.auth.models import User


class Car(models.Model):
    owner = models.ForeignKey(User, on_delete=models.CASCADE,
                              related_name='cars')
    reg_number = models.CharField(max_length=10, blank=False, null=False)
    mot_expire_date = models.DateField(blank=False, null=False)
    make = models.TextField(blank=False, null=False)
    model = models.TextField(blank=False, null=False)
    manufacturing_year = models.TextField()

    def __str__(self) -> str:
        return f"{self.make} {self.model} from {self.manufacturing_year}"
