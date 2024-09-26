from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from .models import User, Realtor

# Define a custom UserAdmin to display additional fields
class CustomUserAdmin(UserAdmin):
    list_display = ('email', 'first_name', 'last_name', 'is_realtor', 'is_staff')
    list_filter = ('is_realtor', 'is_staff')

    fieldsets = (
        (None, {'fields': ('email', 'password')}),
        ('Personal Info', {'fields': ('first_name','last_name')}),
        ('Permissions', {'fields': ('is_staff', 'is_superuser', 'groups', 'user_permissions')}),
        ('Important dates', {'fields': ('last_login', 'created_at')}),
    )

    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('email', 'password1', 'password2'),
        }),
    )

    ordering = ('email',)
    search_fields = ('email', 'first_name', 'phone')

# Register the custom UserAdmin
admin.site.register(User, CustomUserAdmin)


# # Register the Realtor model
# admin.site.register(Realtor)


@admin.register(Realtor)
class RealtorAdmin(admin.ModelAdmin):
      list_display = ('user','profile', 'agency', 'city', 'contact_number')
     






# Register your models here.
