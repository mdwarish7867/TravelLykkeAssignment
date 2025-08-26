from django.urls import path
from . import views

urlpatterns = [
    path('', views.travel_list, name='home'),
    path('travel/', views.travel_list, name='travel_list'),
    path('book/<str:travel_id>/', views.booking_create, name='booking_create'),
    path('bookings/', views.booking_list, name='booking_list'),
    path('bookings/cancel/<str:booking_id>/', views.booking_cancel, name='booking_cancel'),
]