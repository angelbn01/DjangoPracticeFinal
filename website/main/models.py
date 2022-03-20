from django.db.models import Model
from django.db import models
from django.contrib.auth.models import User


class Transport(Model):
    id = models.CharField(max_length=20, unique=True, primary_key=True)
    price = models.FloatField()
    available = models.BooleanField(default=True)


class Scooter(Transport):
    range = models.IntegerField()
    # registration = models.CharField(max_length=7, unique=True, default='0000AAA')


class Bicycle(Transport):
    SIZE_CHOICES = (
        ('adult', 'ADULT'),
        ('child', 'CHILD'),
    )

    size = models.CharField(max_length=5, choices=SIZE_CHOICES)


class ElectricScooter(Transport):
    range = models.IntegerField()
    # registration = models.CharField(max_length=7, unique=True, default='0000AAA')


class Route(Model):
    PLACES = (
        ('green street', 'GREEN STREET'),
        ('blue street', 'BLUE STREET'),
        ('red street', 'RED STREET'),
        ('yellow street', 'YELLOW STREET'),
        ('brown street', 'BROWN STREET'),
        ('black street', 'BLACK STREET'),
    )

    id = models.CharField(max_length=20, unique=True, primary_key=True)
    start_point = models.CharField(max_length=20, choices=PLACES)
    end_point = models.CharField(max_length=20, choices=PLACES)
    start_time = models.DateTimeField()
    km = models.IntegerField()


class MyUser(User):
    vehicle = models.ForeignKey(Transport, on_delete=models.CASCADE, blank=True)
    route = models.ForeignKey(Route, on_delete=models.CASCADE, blank=True)


class Record(Model):
    route = models.ForeignKey(Route, on_delete=models.CASCADE)
    vehicle = models.ForeignKey(Transport, on_delete=models.CASCADE)
    user = models.ForeignKey(MyUser, on_delete=models.CASCADE)
    final_time = models.DateTimeField()
    price = models.FloatField()
