from django.db import models
from django.contrib.auth.models import User
from django.core.validators import MinValueValidator
from django.utils import timezone

class TravelOption(models.Model):
    TRAVEL_TYPES = [
        ('FLIGHT', 'Flight'),
        ('TRAIN', 'Train'),
        ('BUS', 'Bus'),
    ]
    
    travel_id = models.CharField(max_length=10, unique=True)
    travel_type = models.CharField(max_length=10, choices=TRAVEL_TYPES)
    source = models.CharField(max_length=100)
    destination = models.CharField(max_length=100)
    departure_time = models.DateTimeField()
    arrival_time = models.DateTimeField()
    price = models.DecimalField(max_digits=10, decimal_places=2, validators=[MinValueValidator(0)])
    available_seats = models.PositiveIntegerField(default=0)
    
    def __str__(self):
        return f"{self.travel_id} - {self.source} to {self.destination}"
    
    class Meta:
        ordering = ['departure_time']

class Booking(models.Model):
    STATUS_CHOICES = [
        ('CONFIRMED', 'Confirmed'),
        ('CANCELLED', 'Cancelled'),
    ]
    
    booking_id = models.CharField(max_length=10, unique=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    travel_option = models.ForeignKey(TravelOption, on_delete=models.CASCADE)
    number_of_seats = models.PositiveIntegerField(default=1, validators=[MinValueValidator(1)])
    total_price = models.DecimalField(max_digits=10, decimal_places=2, validators=[MinValueValidator(0)])
    booking_date = models.DateTimeField(default=timezone.now)
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='CONFIRMED')
    
    def __str__(self):
        return f"{self.booking_id} - {self.user.username}"
    
    def save(self, *args, **kwargs):
        if not self.booking_id:
            # Generate a unique booking ID
            last_booking = Booking.objects.order_by('-id').first()
            if last_booking:
                last_id = int(last_booking.booking_id[3:])
                new_id = last_id + 1
            else:
                new_id = 1
            self.booking_id = f"BK{new_id:06d}"
        
        # Calculate total price
        if not self.total_price or self.total_price == 0:
            self.total_price = self.travel_option.price * self.number_of_seats
        
        super().save(*args, **kwargs)
    
    class Meta:
        ordering = ['-booking_date']