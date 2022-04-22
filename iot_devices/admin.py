from django.contrib import admin
from .models import Device

# Register your models here.
class DeviceAdmin(admin.ModelAdmin):
    list_display = ['added_by', 'type', 'name', 'device_id',]
    list_filter = ['added_by', 'type', 'device_id',]

admin.site.register(Device, DeviceAdmin)
