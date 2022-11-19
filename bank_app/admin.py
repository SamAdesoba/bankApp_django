from django.contrib import admin
from .models import User
from django.contrib.auth.admin import UserAdmin as AdminUser
# Register your models here.


@admin.register(User)
class UserAdmin(AdminUser):
    add_fieldsets = (
        (
            None,
            {
                "classes": ("wide",),
                "fields": ("email","username", "password1", "password2"),
            },
        ),
    )
