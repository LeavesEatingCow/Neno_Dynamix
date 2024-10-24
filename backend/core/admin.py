from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import User, Address
# Register your models here.
class CustomUserAdmin(UserAdmin):
    fieldsets = UserAdmin.fieldsets + (
        (None, {'fields': ('is_client', 'is_interpreter', 'password_changed')}),
    )

admin.site.register(User, CustomUserAdmin)
admin.site.register(Address)