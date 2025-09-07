from django.shortcuts import render, redirect,get_object_or_404
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.http import Http404
from .models import Movie, Booking,Ticket
import json
from django.http import HttpResponse

# ✅ Mock Movie Data
movies = {
    "Avengers": {"available_seats": 10, "price": 120},
    "Batman": {"available_seats": 8, "price": 150},
    "Spiderman": {"available_seats": 5, "price": 100}
}
movies_data = {
    "Avengers": {"available_seats": 120},
    "Batman": {"available_seats": 120},
    "Spiderman": {"available_seats": 120},
}

# ✅ LOGIN VIEW
def login_view(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user:
            login(request, user)
            return redirect('home')
        else:
            messages.error(request, 'Invalid username or password')
    return render(request, 'login.html')

# ✅ LOGOUT VIEW
def logout_view(request):
    logout(request)
    return redirect('login')

# ✅ HOME PAGE
@login_required
def home(request):
    return render(request, 'home.html', {'movies': movies})

# ✅ BOOK TICKET PAGE
@login_required
def book_ticket_view(request):
    if request.method == "POST":
        # Get movie and seat data from POST
        movie_id = request.POST.get("movie_id")
        movie_list = Movie.objects.all()
        seat_numbers = request.POST.getlist("seats")
        context = {
    'movies': movie_list,
    'range_elite': range(1, 16),
    'range_premium': range(1, 26),
    'range_couple': range(1, 31),
    'range_economy': range(1, 51),
}  # should be a list like ['1', '2', '3']

        # Fetch movie
        movie = Movie.objects.get(id=movie_id)

        # Save the booking
        Booking.objects.create(
            user=request.user,
            movie=movie,
            seat_numbers=", ".join(seat_numbers)  # Store as comma-separated string
        )

        return render(request, 'booked.html', {
            'movie': movie.title,
            'seats': seat_numbers,  # pass the list of seats
        })

    # GET request: show booking form
    movies = Movie.objects.all()
    return render(request, 'book.html', {'movies': movies})


# ✅ CANCEL TICKET VIEW
@login_required
def cancel_ticket(request):
    if request.method == 'POST':
        movie = request.POST.get('movie')
        cancel_count = request.POST.get('cancel_count')
        try:
            count = int(cancel_count)
            if movie in movies_data:
                movies_data[movie]['available_seats'] += count
                return redirect('movies')
        except:
            return render(request, 'cancel.html', {'movies': movies_data, 'error': 'Invalid number'})
    return render(request, 'cancel.html', {'movies': movies_data})

# ✅ VIEW: AVAILABLE MOVIES
@login_required
def available_movies(request):
    return render(request, 'movies.html', {'movies': movies_data})

# ✅ SELECT SEATS VIEW (redirect)
@login_required
def select_seats(request):
    if request.method == "POST":
        movie = request.POST.get("movie").lower()
        return redirect('movie_seats', movie_name=movie)
    return redirect('book')

@login_required
def movie_seats(request, movie_name):
    movie_name = movie_name.lower()
    if movie_name == "avengers":
        return avengers_seats(request)
    elif movie_name == "batman":
        return batman_seats(request)
    elif movie_name == "spiderman":
        return spiderman_seats(request)


# ✅ SPIDERMAN SEAT PAGE
@login_required
def spiderman_seats(request):
    return render(request, 'seats/spiderman_seats.html', {
        'elite_count': 15,
        'premium_count': 25,
        'couple_count': 30,
        'economy_count': 50,
        'sold_seats': [],  # sample sold seats
    })

# ✅ BATMAN SEAT PAGE
@login_required
def batman_seats(request):
    return render(request, 'seats/batman_seats.html', {
        'elite_count': 15,
        'premium_count': 25,
        'couple_count': 30,
        'economy_count': 50,
        'sold_seats': [],  # sample sold seats
    })

# ✅ AVENGERS SEAT PAGE
@login_required
def avengers_seats(request):
    return render(request, 'seats/avengers_seats.html', {
        'elite_count': 15,
        'premium_count': 25,
        'couple_count': 30,
        'economy_count': 50,
        'sold_seats': [],  # sample sold seats
    })

SOLD_SEATS = set() 
# ✅ BOOKED PAGE VIEW FOR EACH MOVIE
@login_required
def book_avengers(request):
    if request.method == "POST":
        # get movie
        try:
            movie = Movie.objects.get(name="Avengers")
        except Movie.DoesNotExist:
            return HttpResponse("Movie not found")

        # get selected seat(s)
        selected_seats = request.POST.getlist("selected_seats")

        for seat in selected_seats:
            Ticket.objects.create(movie=movie, seat_number=seat)

        return redirect("booking-success")
    return HttpResponse("Invalid request")


@login_required
def book_batman(request):
    return render(request, 'seats/booked.html', {'movie': 'Batman'})

@login_required
def book_spiderman(request):
    return render(request, 'seats/booked.html', {'movie': 'Spiderman'})

@login_required
def book_avengers(request):
    return render(request, 'seats/booked.html', {'movie': 'avengers'})

# ✅ SIDEBAR ROUTES (Optional Pages)
@login_required
def account(request): return render(request, 'base/sidebar/account.html')
@login_required
def settings(request): return render(request, 'base/sidebar/settings.html')
@login_required
def notifications(request): return render(request, 'base/sidebar/notifications.html')
@login_required
def rewards(request): return render(request, 'base/sidebar/rewards.html')
@login_required
def support(request): return render(request, 'base/sidebar/support.html')
@login_required
def orders(request): return render(request, 'base/sidebar/orders.html')
