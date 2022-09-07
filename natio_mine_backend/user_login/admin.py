from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from .forms import CustomUserChangeForm, CustomUserCreationForm
from .models import CustomUser

class CustomUserAdmin(UserAdmin):
    add_form = CustomUserCreationForm
    form = CustomUserChangeForm
    model = CustomUser
    list_display = ['username', 'profile', ]
    fieldsets = UserAdmin.fieldsets + (
            (None, {'fields': ('profile', )}),
    ) #this will allow to change these fields in admin module


admin.site.register(CustomUser, CustomUserAdmin)