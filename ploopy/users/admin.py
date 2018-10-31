from django.contrib import admin
from django.contrib.auth import admin as auth_admin
from .models import User
from ploopy.users.forms import UserChangeForm, UserCreationForm


@admin.register(User)
class UserAdmin(auth_admin.UserAdmin):

    form = UserChangeForm
    add_form = UserCreationForm
    fieldsets = (
                    ("User Profile", {"fields": ('name','followers','following','profile_image','website','gender','bio')}),
                ) + auth_admin.UserAdmin.fieldsets
    list_display = ["username", "name", "is_superuser"]
    search_fields = ["name"]
