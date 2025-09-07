from django.db import models
from django.utils import timezone

# Create your models here.

class moviesticketbooking:
    def __init__(self):
        self.movies = {
            "Avengers": {"available_seats": 10, "price": 120},
            "Batman": {"available_seats": 8, "price": 150},
            "Spiderman": {"available_seats": 5, "price": 100}
        }

from django.contrib.auth.models import User

# Movie model
from django.db import models

class Ticket(models.Model):
    movie = models.ForeignKey("Movie", on_delete=models.CASCADE)
    seat_number = models.CharField(max_length=100,default='none')
    booked_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.movie} - {self.seat_number}"

class Movie(models.Model):
    name = models.CharField(max_length=100, default="Untitled Movie")
    title = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=6, decimal_places=2)
    show_time = models.DateTimeField(default=timezone.now)
    elite_seats = models.IntegerField(default=0)
    premium_seats = models.IntegerField(default=0)
    couple_seats = models.IntegerField(default=0)
    economy_seats = models.IntegerField(default=0)
    price = models.DecimalField(max_digits=6, decimal_places=2)
    description = models.TextField( null = True, blank=True)
    duration = models.DurationField(blank=True, null=True)
    show_time = models.DateTimeField()
    price = models.PositiveIntegerField()
    total_seats = models.PositiveIntegerField(default=100)
    available_seats = models.PositiveIntegerField()

    def available_seats(self):
        return self.elite_seats + self.premium_seats + self.couple_seats + self.economy_seats

    def __str__(self):
        return self.title


# Booking model
from django.contrib.auth.models import User

class Booking(models.Model):
    CATEGORY_CHOICES = [
        ('ELITE', 'Elite'),
        ('PREMIUM', 'Premium'),
        ('COUPLE', 'Couple'),
        ('ECONOMY', 'Economy'),
    ]

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE)
    category = models.CharField(max_length=10, choices=CATEGORY_CHOICES)
    tickets_booked = models.PositiveIntegerField()
    seat_numbers = models.JSONField(default='none')  # Store as list: ["A1", "A2", ...]
    booking_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.user.username} - {self.movie.title} - {self.category}"


# Cancellation model (Optional, can be merged with Booking if not needed separately)
class Cancellation(models.Model):
    booking = models.ForeignKey(Booking, on_delete=models.CASCADE)
    tickets_cancelled = models.PositiveIntegerField()
    cancelled_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Cancelled {self.tickets_cancelled} from {self.booking}"
    


