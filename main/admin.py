from django.contrib import admin
from .models import Appointment

@admin.register(Appointment)
class AppointmentAdmin(admin.ModelAdmin):
    list_display = ('name', 'phone', 'service', 'created_at')
    list_filter = ('service', 'created_at')
    search_fields = ('name', 'phone')