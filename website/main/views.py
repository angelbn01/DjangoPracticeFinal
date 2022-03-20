from django.shortcuts import render

from .models import *


# Create your views here.

def home(request):
    bicycles = Bicycle.objects.all()
    scooters = Scooter.objects.all()
    electric_scooters = ElectricScooter.objects.all()
    return render(request, 'main/home.html', {'bicycles': bicycles, 'scooters': scooters, 'electric_scooters': electric_scooters})


def transports(request):
    return render(request, 'main/home.html')
