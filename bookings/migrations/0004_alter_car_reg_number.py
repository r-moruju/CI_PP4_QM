# Generated by Django 3.2.16 on 2023-02-05 11:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bookings', '0003_rename_model_car_color'),
    ]

    operations = [
        migrations.AlterField(
            model_name='car',
            name='reg_number',
            field=models.CharField(max_length=10, unique=True),
        ),
    ]
