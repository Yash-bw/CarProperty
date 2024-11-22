from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import User

# Define a custom UserAdmin to add custom fields to the Django Admin
class CustomUserAdmin(UserAdmin):
    model = User
    list_display = ['username', 'first_name', 'last_name', 'email', 'phone_number', 'address', 'date_of_birth', 'role']
    list_filter = ['role']
    fieldsets = UserAdmin.fieldsets + (
        (None, {'fields': ('phone_number', 'address', 'profile_picture', 'date_of_birth')}),
    )
    add_fieldsets = UserAdmin.add_fieldsets + (
        (None, {'fields': ('phone_number', 'address', 'profile_picture', 'date_of_birth')}),
    )
    search_fields = ('username', 'email', 'phone_number')

# Register the custom User model with the custom UserAdmin
admin.site.register(User, CustomUserAdmin)
