from django.core.exceptions import PermissionDenied
from django.shortcuts import render
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required
from django.views.generic.edit import CreateView, UpdateView
from . import forms

from .models import *


# Create your views here.

class LoginRequiredMixin(object):
    @method_decorator(login_required())
    def dispatch(self, *args, **kwargs):
        return super(LoginRequiredMixin, self).dispatch(*args, **kwargs)


class CheckIsOwnerMixin(object):
    def get_object(self, *args, **kwargs):
        obj = super(CheckIsOwnerMixin, self).get_object(*args, **kwargs)
        if not obj.user == self.request.user:
            raise PermissionDenied
        return obj


class LoginRequiredCheckIsOwnerUpdateView(LoginRequiredMixin, CheckIsOwnerMixin, UpdateView):
    template_name = 'main/form.html'


def home(request):
    bicycles = Bicycle.objects.all()
    scooters = Scooter.objects.all()
    electric_scooters = ElectricScooter.objects.all()
    routes = Route.objects.all()
    records = Record.objects.all()
    users = User.objects.all()
    return render(request, 'main/home.html', {'bicycles': bicycles, 'scooters': scooters, 'electric_scooters': electric_scooters, 'routes': routes, 'records': records, 'users': users})


def transports(request):
    return render(request, 'main/home.html')


class RouteCreate(LoginRequiredMixin, CreateView):
    model = Route
    template_name = 'main/form.html'
    form_class = forms.RouteForm

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super(RouteCreate, self).form_valid(form)