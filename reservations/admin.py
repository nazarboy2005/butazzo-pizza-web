from django.contrib import admin
from reservations.models import ReservationsModel


@admin.register(ReservationsModel)

class ReservationsModelAdmin(admin.ModelAdmin):
    search_fields = ['full_name', 'date', 'created_at', 'updated_at', 'time']
    list_display = ['full_name', 'phone_number', 'date', 'time', 'created_at']