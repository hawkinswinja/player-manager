from django.urls import path, include
from django.contrib.auth import views as auth_views
from django.contrib.auth.decorators import login_required

from . import views

urlpatterns = [
    path("status/", views.status, name="test"),
    path(
        "accounts/login/",
        auth_views.LoginView.as_view(template_name="login.html"),
        name="login",
    ),
    path(
        "accounts/logout/",
        auth_views.LogoutView.as_view(next_page="/accounts/login"),
        name="logout",
    ),
    path("counties/", login_required(views.counties), name="counties"),
    path("counties/<str:county>", login_required(views.county), name="county"),
    path("academies/<str:academy>", login_required(views.academy), name="academy"),
]
