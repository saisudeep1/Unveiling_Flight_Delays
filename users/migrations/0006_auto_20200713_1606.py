# Generated by Django 2.0.13 on 2020-07-13 10:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0005_auto_20200713_1254'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='flightdatamodel',
            name='AIRLINE',
        ),
        migrations.RemoveField(
            model_name='flightdatamodel',
            name='AIRLINE_DELAY',
        ),
        migrations.RemoveField(
            model_name='flightdatamodel',
            name='AIR_SYSTEM_DELAY',
        ),
        migrations.RemoveField(
            model_name='flightdatamodel',
            name='AIR_TIME',
        ),
        migrations.RemoveField(
            model_name='flightdatamodel',
            name='ARRIVAL_DELAY',
        ),
        migrations.RemoveField(
            model_name='flightdatamodel',
            name='ARRIVAL_TIME',
        ),
        migrations.RemoveField(
            model_name='flightdatamodel',
            name='CANCELLATION_REASON',
        ),
        migrations.RemoveField(
            model_name='flightdatamodel',
            name='CANCELLED',
        ),
        migrations.RemoveField(
            model_name='flightdatamodel',
            name='DEPARTURE_DELAY',
        ),
        migrations.RemoveField(
            model_name='flightdatamodel',
            name='DISTANCE',
        ),
        migrations.RemoveField(
            model_name='flightdatamodel',
            name='DIVERTED',
        ),
        migrations.RemoveField(
            model_name='flightdatamodel',
            name='ELAPSED_TIME',
        ),
        migrations.RemoveField(
            model_name='flightdatamodel',
            name='LATE_AIRCRAFT_DELAY',
        ),
        migrations.RemoveField(
            model_name='flightdatamodel',
            name='MONTH',
        ),
        migrations.RemoveField(
            model_name='flightdatamodel',
            name='SCHEDULED_ARRIVAL',
        ),
        migrations.RemoveField(
            model_name='flightdatamodel',
            name='SCHEDULED_DEPARTURE',
        ),
        migrations.RemoveField(
            model_name='flightdatamodel',
            name='SCHEDULED_TIME',
        ),
        migrations.RemoveField(
            model_name='flightdatamodel',
            name='SECURITY_DELAY',
        ),
        migrations.RemoveField(
            model_name='flightdatamodel',
            name='TAIL_NUMBER',
        ),
        migrations.RemoveField(
            model_name='flightdatamodel',
            name='TAXI_IN',
        ),
        migrations.RemoveField(
            model_name='flightdatamodel',
            name='WEATHER_DELAY',
        ),
        migrations.RemoveField(
            model_name='flightdatamodel',
            name='WHEELS_OFF',
        ),
        migrations.RemoveField(
            model_name='flightdatamodel',
            name='WHEELS_ON',
        ),
        migrations.RemoveField(
            model_name='flightdatamodel',
            name='YEAR',
        ),
        migrations.AlterField(
            model_name='flightdatamodel',
            name='DESTINATION_AIRPORT',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='flightdatamodel',
            name='ORIGIN_AIRPORT',
            field=models.CharField(max_length=100),
        ),
    ]