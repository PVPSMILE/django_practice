from django.contrib import admin

from login.models import CustomUser

# Register your models here.
@admin.register(CustomUser)
class CustomUserAdmin(admin.ModelAdmin):
    list_display = ('username', 'email', 'phone', 'is_admin', 'is_staff', 'is_email_verified')
    search_fields = ('username', 'email', 'phone')
    list_filter = ('is_admin', 'is_staff', 'is_email_verified')