from django.shortcuts import render, redirect, resolve_url
from .forms import CountyForm, AcademyForm, PlayerForm
from django.contrib.auth import get_user_model, get_user
from .util import DB
from django.http import JsonResponse


def home(request):
    """
    GET: returns a response with status 302
    description: perform redirects based on user role
    """
    user = get_user(request)
    if user and user.name:
        if user.role == "academy":
            return redirect(f"/academies/{user.name}")
        elif user.role == "county":
            return redirect(f"/counties/{user.name}")
        return redirect("/counties")
    return redirect("/")


def status(request):
    """
    GET: returns a response with status 200
    description: check for server status
    """
    return JsonResponse({"status": "success"}, status=200)


def counties(request):
    """
    POST: creates a new county under management
    GET: - returns the profile page with links to each county
         - if args, delete the county passed in args
    """
    form = CountyForm()
    if request.method == "POST":
        form = CountyForm(request.POST)
        if form.is_valid():
            try:
                data = form.save(commit=False)
                # create the user access for managing this resource
                DB.create_admin(data.name, "county", data.password)
                data.save()
                form = CountyForm()
            except Exception as e:
                form.add_error(str(e))
    elif request.GET:
        name = request.GET["county"]
        DB.delete_instance("County", name=name)
        DB.delete_instance("Admin", name=name, role="county")

    counties = DB.all_instances("County")
    return render(request, "counties.html", {"form": form, "counties": counties})


def county(request, county):
    """
    POST: creates a new academy for this county
    GET: - returns the profile page for the county
         - if args, delete the academy passed as arg
    """
    form = AcademyForm()
    if request.method == "POST":
        form = AcademyForm(request.POST)
        if form.is_valid():
            try:
                data = form.save(commit=False)

                # create the user access for managing this resource
                DB.create_admin(data.name, "academy", data.password)
                data.save()
                form = AcademyForm()
            except Exception as e:
                form.add_error(str(e))
    elif request.GET:
        name = request.GET["academy"]
        DB.delete_instance("Academy", name=name)
        DB.delete_instance("Admin", name=name, role="academy")

    county_instance = DB.get_instance("County", "name", county)
    academies = DB.all_instances("Academy", "county", county_instance)
    return render(
        request, "county_academies.html", {"form": form, "academies": academies}
    )


def academy(request, academy):
    """
    POST: creates a new academy for this county
    GET: - returns the profile page for the county by default
      - if args, delete the academy player passed in arg
    """
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
