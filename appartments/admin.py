from django.contrib import admin
from .models import Object, Appartments
# Register your models here.

@admin.register(Object)
class ObjectAdmin(admin.ModelAdmin):
    list_display = [
        'title'
    ]

@admin.register(Appartments)
class AppartmentAdmin(admin.ModelAdmin):
    list_display = [
        'object',
        'floor',
        'kv',
        'status',
        'price',
        'customer',
        'end_time',
        'date'
    ]