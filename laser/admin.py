from django.contrib import admin
from .models import Manual, Software, SparePart, Equipment

# Register your models here.


@admin.register(Manual)
class ManualAdmin(admin.ModelAdmin):
    list_display = ('name', 'type', 'created', 'modify')


@admin.register(Software)
class SoftwareAdmin(admin.ModelAdmin):
    list_display = ('name', 'type', 'created', 'modify')


@admin.register(SparePart)
class SparePartAdmin(admin.ModelAdmin):
    list_display = ('name', 'type', 'created', 'modify')


@admin.register(Equipment)
class EquipmentAdmin(admin.ModelAdmin):
    list_display = ('name', 'type', 'created', 'modify')
