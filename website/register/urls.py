from django.urls import path
from django.contrib import admin
from . import views
from django.contrib.auth import views as views2


urlpatterns = [
    path('accounts/login/', views2.LoginView.as_view(), name='login'),
    path('accounts/logout/', views2.LogoutView.as_view(), name='logout'),
    path('register/', views.register)
]
