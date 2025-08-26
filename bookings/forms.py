from django import forms
from .models import TravelOption, Booking

class TravelSearchForm(forms.Form):
    TRAVEL_TYPES = [
        ('', 'All'),
        ('FLIGHT', 'Flight'),
        ('TRAIN', 'Train'),
        ('BUS', 'Bus'),
    ]
    
    travel_type = forms.ChoiceField(choices=TRAVEL_TYPES, required=False)
    source = forms.CharField(max_length=100, required=False)
    destination = forms.CharField(max_length=100, required=False)
    date = forms.DateField(required=False, widget=forms.DateInput(attrs={'type': 'date'}))

class BookingForm(forms.ModelForm):
    class Meta:
        model = Booking
        fields = ['number_of_seats']
        widgets = {
            'number_of_seats': forms.NumberInput(attrs={'min': 1}),
        }
    
    def __init__(self, *args, **kwargs):
        self.travel_option = kwargs.pop('travel_option', None)
        super().__init__(*args, **kwargs)
    
    def clean_number_of_seats(self):
        number_of_seats = self.cleaned_data.get('number_of_seats')
        if self.travel_option and number_of_seats > self.travel_option.available_seats:
            raise forms.ValidationError(f"Only {self.travel_option.available_seats} seats available.")
        return number_of_seats