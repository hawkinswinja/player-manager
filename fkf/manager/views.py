from django.shortcuts import render, redirect, resolve_url
from .forms import CountyForm, AcademyForm, PlayerForm

# from .models import County, Academy, Player
from .util import DB
from django.http import JsonResponse


def status(request):
    return JsonResponse({"status": "success"}, status=200)


def login(request):
    return render(request, "login.html", {"status": True})


def counties(request):
    form = CountyForm()
    if request.method == "POST":
        form = CountyForm(request.POST)
        if form.is_valid():
            try:
                form.save()
                form = CountyForm()
            except Exception as e:
                form.add_error(str(e))
    elif request.GET:
        name = request.GET["county"]
        DB.delete_instance("County", "name", name)

    counties = DB.all_instances("County")
    return render(request, "counties.html", {"form": form, "counties": counties})


def county(request, county):
    form = AcademyForm()
    if request.method == "POST":
        form = AcademyForm(request.POST)
        if form.is_valid():
            try:
                form.save()
                form = AcademyForm()
            except Exception as e:
                form.add_error(str(e))
    elif request.GET:
        name = request.GET["academy"]
        DB.delete_instance("Academy", "name", name)

    county_instance = DB.get_instance("County", "name", county)
    academies = DB.all_instances("Academy", "county", county_instance)
    return render(
        request, "county_academies.html", {"form": form, "academies": academies}
    )


def academy(request, academy):
    form = PlayerForm()
    if request.method == "POST":
        form = PlayerForm(request.POST, request.FILES)
        if form.is_valid():
            try:
                form.save()
                form = PlayerForm()
            except Exception as e:
                form.add_error(None, str(e))
    elif request.GET:
        pid = request.GET["pid"]
        DB.delete_instance("Player", "pid", pid)

    academy_instance = DB.get_instance("Academy", "name", academy)
    players = DB.all_instances("Player", "academy", academy_instance)
    return render(
        request, "academy.html", {"form": form, "players": players, "academy": academy}
    )
