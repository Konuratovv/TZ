from django.contrib import admin
from django.contrib.auth.models import Group
from .models import Managers

# Register your models here.

admin.site.unregister(Group)

@admin.register(Managers)
class ManagersAdmin(admin.ModelAdmin):
    list_display = [
        'name',
        'phone_number',
        'email',
        'created_at',
    ]

    readonly_fields = [
        'transactions_count',
        'password',
    ]