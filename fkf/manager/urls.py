from django.urls import path

from . import views

urlpatterns = [
    path("status/", views.status, name="test"),
    path("counties/", views.get_county, name="counties"),
]
