from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from users.models import User


class Admin(UserAdmin):
    """"""

    model = User
    list_display = ["email", "nickname", "is_staff", "is_superuser", "is_active"]
    list_filter = ["email"]
    # custom fields that can be used for querying
    fieldsets = [
        (None, {"fields": ["email", "password"]}),
        ("Nickname", {"fields": ["nickname"]}),
        ("Permissions", {"fields": ["is_staff"]}),
    ]
    # custom fields that can be used for user creation
    add_fieldsets = [
        (None, {"fields": ["email", "nickname", "password1", "password2"]})
    ]
    search_fields = ["email"]
    ordering = ["email"]


admin.site.register(User, Admin)
