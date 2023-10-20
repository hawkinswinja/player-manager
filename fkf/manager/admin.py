from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import County, Academy, Player, Admin
from .forms import AddUser


class CustomUserAdmin(UserAdmin):
    fieldsets = (
        (None, {"fields": ("name", "password", "role")}),
        (
            "Permissions",
            {
                "fields": (
                    "is_active",
                    "is_staff",
                    "is_superuser",
                    "groups",
                    "user_permissions",
                )
            },
        ),
    )
    add_fieldsets = (
        (
            None,
            {
                "classes": ("wide",),
                "fields": ("name", "password1", "password2", "role"),
            },
        ),
    )

    list_display = ("name", "role", "is_staff")
    list_filter = ("is_staff", "is_superuser", "is_active", "groups")

    search_fields = ("name",)
    ordering = ("name",)
    filter_horizontal = (
        "groups",
        "user_permissions",
    )


admin.site.register(County)
admin.site.register(Academy)
admin.site.register(Player)
admin.site.register(Admin, CustomUserAdmin)
