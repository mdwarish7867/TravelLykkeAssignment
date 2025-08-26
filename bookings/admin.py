from django.contrib import admin
from .models import TravelOption, Booking

@admin.register(TravelOption)
class TravelOptionAdmin(admin.ModelAdmin):
    list_display = ('travel_id', 'travel_type', 'source', 'destination', 'departure_time', 'price', 'available_seats')
    list_filter = ('travel_type', 'source', 'destination')
    search_fields = ('travel_id', 'source', 'destination')
    ordering = ('departure_time',)

@admin.register(Booking)
class BookingAdmin(admin.ModelAdmin):
    list_display = ('booking_id', 'user', 'travel_option', 'number_of_seats', 'total_price', 'booking_date', 'status')
    list_filter = ('status', 'booking_date', 'travel_option__travel_type')
    search_fields = ('booking_id', 'user__username', 'travel_option__travel_id')
    ordering = ('-booking_date',)