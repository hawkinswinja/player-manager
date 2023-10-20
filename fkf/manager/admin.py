from django.contrib import admin

# from django.contrib.auth.admin import UserAdmin
from .models import County, Academy, Player, Admin

admin.site.register(County)
admin.site.register(Academy)
admin.site.register(Player)
admin.site.register(Admin)
