# Generated by Django 3.2.16 on 2023-02-08 12:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bookings', '0005_car_booked'),
    ]

    operations = [
        migrations.AlterField(
            model_name='booking',
            name='date',
            field=models.DateTimeField(),
        ),
    ]