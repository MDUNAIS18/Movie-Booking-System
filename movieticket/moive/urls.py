from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),                         
    path('login/', views.login_view, name='login'),  
    path('logout/', views.logout_view, name='logout'),
    path('book/', views.book_ticket_view, name='book'),
    path('cancel/', views.cancel_ticket, name='cancel'), 
    path('movies/', views.available_movies, name='movies'),
    path('select_seats/', views.select_seats, name='select_seats'),
    path('seats/<str:movie_name>/', views.movie_seats, name='movie_seats'),
    path('account/', views.account, name='account'),
    path('settings/', views.settings, name='settings'),
    path('notifications/', views.notifications, name='notifications'),
    path('rewards/', views.rewards, name='rewards'),
    path('support/', views.support, name='support'),
    path('orders/', views.orders, name='orders'),
    path('seats/spiderman/', views.spiderman_seats, name='spiderman-seats'),
    path('seats/batman/', views.batman_seats, name='batman-seats'),
    path('seats/avengers/', views.avengers_seats, name='avengers-seats'),
    path('book/avengers/', views.book_avengers, name='book-avengers'),
    path('book/batman/', views.book_batman, name='book-batman'),
    path('book/spiderman/', views.book_spiderman, name='book-spiderman'),
    

]
