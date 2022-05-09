from django.urls import path
from django.views.generic import RedirectView

from . import views

from .views import RouteDetail

app_name = 'main'

urlpatterns = [
    path("", RedirectView.as_view(pattern_name='main:home')),
    path("home/", views.home, name='home'),
    path("transports/", views.transports),
    path("create/", views.RouteCreate.as_view()),
    path("routes/ <str:pk>",
        RouteDetail.as_view(),
        name='route_detail'),
    path('routes/ <str:pk>/delete/', views.RouteDelete.as_view(), name='route_delete'),
]