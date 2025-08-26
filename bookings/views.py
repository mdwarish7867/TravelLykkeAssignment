from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.db.models import Q
from django.core.paginator import Paginator
from .models import TravelOption, Booking
from .forms import TravelSearchForm, BookingForm

def travel_list(request):
    travel_options = TravelOption.objects.all()
    form = TravelSearchForm(request.GET or None)
    
    if form.is_valid():
        travel_type = form.cleaned_data.get('travel_type')
        source = form.cleaned_data.get('source')
        destination = form.cleaned_data.get('destination')
        date = form.cleaned_data.get('date')
        
        if travel_type:
            travel_options = travel_options.filter(travel_type=travel_type)
        if source:
            travel_options = travel_options.filter(source__icontains=source)
        if destination:
            travel_options = travel_options.filter(destination__icontains=destination)
        if date:
            travel_options = travel_options.filter(departure_time__date=date)
    
    # Pagination
    paginator = Paginator(travel_options, 10)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    
    context = {
        'form': form,
        'page_obj': page_obj,
    }
    
    return render(request, 'bookings/travel_list.html', context)

@login_required
def booking_create(request, travel_id):
    travel_option = get_object_or_404(TravelOption, travel_id=travel_id)
    
    if request.method == 'POST':
        form = BookingForm(request.POST, travel_option=travel_option)
        if form.is_valid():
            booking = form.save(commit=False)
            booking.user = request.user
            booking.travel_option = travel_option
            booking.total_price = travel_option.price * form.cleaned_data['number_of_seats']
            booking.save()
            
            # Update available seats
            travel_option.available_seats -= form.cleaned_data['number_of_seats']
            travel_option.save()
            
            messages.success(request, 'Booking confirmed successfully!')
            return redirect('booking_list')
    else:
        form = BookingForm(travel_option=travel_option)
    
    context = {
        'form': form,
        'travel_option': travel_option,
    }
    
    return render(request, 'bookings/booking_form.html', context)

@login_required
def booking_list(request):
    bookings = Booking.objects.filter(user=request.user).order_by('-booking_date')
    
    # Separate upcoming and past bookings
    upcoming_bookings = bookings.filter(
        travel_option__departure_time__gte=timezone.now(),
        status='CONFIRMED'
    )
    past_bookings = bookings.exclude(
        travel_option__departure_time__gte=timezone.now(),
        status='CONFIRMED'
    )
    
    context = {
        'upcoming_bookings': upcoming_bookings,
        'past_bookings': past_bookings,
    }
    
    return render(request, 'bookings/booking_list.html', context)

@login_required
def booking_cancel(request, booking_id):
    booking = get_object_or_404(Booking, booking_id=booking_id, user=request.user)
    
    if request.method == 'POST':
        # Restore available seats
        travel_option = booking.travel_option
        travel_option.available_seats += booking.number_of_seats
        travel_option.save()
        
        # Cancel booking
        booking.status = 'CANCELLED'
        booking.save()
        
        messages.success(request, 'Booking cancelled successfully!')
        return redirect('booking_list')
    
    context = {
        'booking': booking,
    }
    
    return render(request, 'bookings/booking_cancel.html', context)