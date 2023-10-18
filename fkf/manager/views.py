from django.shortcuts import render, redirect

# from .models import County, Academy, Player
from .util import DB
from django.http import JsonResponse


def status(request):
    return JsonResponse({"status": "success"}, status=200)


def add_county(request):
    if request.method == "POST":
        name = request.POST["name"]
        admin = request.POST["admin"]
        password = request.POST["password"]
        DB.create_county(name, admin, password)
        return redirect("county_list")  # Redirect to the list of counties view
    return render(request, "add_county.html")


def delete_county(request, county_id):
    if request.method == "POST":
        DB.delete_instance("County", "id", county_id)
        return redirect("county_list")  # Redirect to the list of counties view


def update_county(request, county_id):
    if request.method == "POST":
        admin = request.POST["admin"]
        password = request.POST["password"]
        DB.update_instance("County", "id", county_id, admin=admin, password=password)
        return redirect("county_list")  # Redirect to the list of counties view


def get_county(request, name=None):
    counties = DB.all_instances("County", "name", name)
    return render(request, "county_admin.html", {"counties": counties})


# Implement similar views for Academy and Player
