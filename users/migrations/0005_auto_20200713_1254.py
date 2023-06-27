# Generated by Django 2.0.13 on 2020-07-13 07:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0004_auto_20200713_1229'),
    ]

    operations = [
        migrations.AlterField(
            model_name='flightdatamodel',
            name='AIRLINE',
            field=models.CharField(default=None, max_length=200),
        ),
        migrations.AlterField(
            model_name='flightdatamodel',
            name='CANCELLATION_REASON',
            field=models.CharField(default=None, max_length=20),
        ),
        migrations.AlterField(
            model_name='flightdatamodel',
            name='CANCELLED',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='flightdatamodel',
            name='DAY',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='flightdatamodel',
            name='DAY_OF_WEEK',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='flightdatamodel',
            name='DESTINATION_AIRPORT',
            field=models.CharField(default=None, max_length=200),
        ),
        migrations.AlterField(
            model_name='flightdatamodel',
            name='DISTANCE',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='flightdatamodel',
            name='DIVERTED',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='flightdatamodel',
            name='FLIGHT_NUMBER',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='flightdatamodel',
            name='MONTH',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='flightdatamodel',
            name='ORIGIN_AIRPORT',
            field=models.CharField(default=None, max_length=200),
        ),
        migrations.AlterField(
            model_name='flightdatamodel',
            name='SCHEDULED_ARRIVAL',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='flightdatamodel',
            name='SCHEDULED_DEPARTURE',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='flightdatamodel',
            name='SCHEDULED_TIME',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='flightdatamodel',
            name='TAIL_NUMBER',
            field=models.CharField(default=None, max_length=200),
        ),
        migrations.AlterField(
            model_name='flightdatamodel',
            name='WEATHER_DELAY',
            field=models.FloatField(default=0.0),
        ),
        migrations.AlterField(
            model_name='flightdatamodel',
            name='YEAR',
            field=models.IntegerField(default=0),
        ),
    ]