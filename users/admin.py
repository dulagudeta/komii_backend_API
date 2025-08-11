from django.contrib import admin
from .models import User
from django.contrib.auth.admin import UserAdmin 

# Register your models here.
admin.site.register(User, UserAdmin)
@admin.register(User)
class CustomUserAdmin(UserAdmin):
    list_display = ('username', 'email', 'role', 'is_approved', 'is_staff')
    list_filter = ('role', 'is_approved', 'is_staff')
    search_fields = ('username', 'email')