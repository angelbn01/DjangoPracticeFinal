from django.forms import ModelForm
from . import models


class RouteForm(ModelForm):
    class Meta:
        model = models.Route
        exclude = ('user',)
