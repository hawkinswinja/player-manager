from django.urls import path

from . import views

urlpatterns = [
    path("status/", views.status, name="test"),
    path("home/", views.login, name="login"),
    path("counties/", views.counties, name="counties"),
    path("counties/<str:county>", views.county, name="county"),
    path("academies/<str:academy>", views.academy, name="academy"),
]
