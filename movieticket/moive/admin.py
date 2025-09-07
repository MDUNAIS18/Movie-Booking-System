from django.contrib import admin
from .models import Movie, Booking, Cancellation

@admin.register(Movie)
class MovieAdmin(admin.ModelAdmin):
    list_display = ['title', 'price', 'elite_seats', 'show_time' , 'premium_seats', 'couple_seats', 'economy_seats', 'total_seats']
    search_fields = ['title']
    list_filter = ['show_time']

@admin.register(Booking)
class BookingAdmin(admin.ModelAdmin):
    list_display = ['user', 'movie', 'category', 'tickets_booked', 'booking_date']
    list_filter = ['movie', 'category', 'booking_date']
    search_fields = ['user__username', 'movie__title']

@admin.register(Cancellation)
class CancellationAdmin(admin.ModelAdmin):
    list_display = ['get_user', 'get_movie', 'tickets_cancelled', 'cancelled_at']
    list_filter = ['booking__movie', 'cancelled_at']

    def get_user(self, obj):
        return obj.booking.user
    get_user.short_description = 'User'

    def get_movie(self, obj):
        return obj.booking.movie
    get_movie.short_description = 'Movie'
