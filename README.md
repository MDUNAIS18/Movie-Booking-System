Movie Ticket Booking System:
A Django-based web application for booking movie tickets, managing seat selection, and handling user accounts.

Features
User authentication (login/logout)
Movie listing and details
Seat selection for different categories (Elite, Premium, Couple, Economy)
Ticket booking and cancellation
Admin interface for managing movies, bookings, and cancellations
Sidebar for user account, notifications, orders, rewards, and support
Project Structure
models.py: Defines database models for Movie, Ticket, Booking, and Cancellation.
views.py: Contains all the logic for user interaction, booking, seat selection, and sidebar pages.
admin.py: Customizes the Django admin interface for managing the app.
templates/: HTML templates for all pages (login, booking, seats, sidebar, etc.)
static/: Static files (images, CSS, etc.)
Main Methods and Their Purpose
Models (models.py)
Movie: Stores movie details, seat categories, prices, and show times.

__str__: Returns the movie title.
available_seats: Calculates total available seats by category.
Ticket: Represents a booked seat for a movie.

__str__: Returns a string with movie and seat number.
Booking: Stores user bookings, including seat numbers and category.

__str__: Returns a string with user, movie, and category.
Cancellation: Tracks ticket cancellations.

__str__: Returns a string describing the cancellation.
Views (views.py)
login_view: Handles user login.
logout_view: Handles user logout.
home: Displays the home page with available movies.
book_ticket_view: Handles ticket booking, seat selection, and saving bookings.
cancel_ticket: Allows users to cancel booked tickets.
available_movies: Shows all available movies.
select_seats: Redirects to the seat selection page for a chosen movie.
movie_seats: Redirects to the correct seat selection view based on movie.
spiderman_seats, batman_seats, avengers_seats: Render seat selection pages for each movie.
book_avengers, book_batman, book_spiderman: Handle booking confirmation for each movie.
account, settings, notifications, rewards, support, orders: Render sidebar pages for user account management.
Admin (admin.py)
MovieAdmin: Customizes movie display, search, and filtering in admin.
BookingAdmin: Customizes booking display, search, and filtering in admin.
CancellationAdmin: Customizes cancellation display, search, and filtering in admin.
get_user: Returns the user for a cancellation.
get_movie: Returns the movie for a cancellation.
How to Run
Clone the repository.
Install dependencies: pip install -r requirements.txt
Run migrations: python manage.py migrate
Create a superuser: python manage.py createsuperuser
Start the server: python manage.py runserver
Access the app at http://127.0.0.1:8000/
Screenshots
(Add screenshots of your app here)

License
MIT
