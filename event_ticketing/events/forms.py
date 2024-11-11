from django import forms
from .models import Event, Ticket

class EventForm(forms.ModelForm):
    class Meta:
        model = Event
        fields = ['name', 'date', 'location', 'description']

class TicketForm(forms.ModelForm):
    class Meta:
        model = Ticket
        fields = ['buyer_name', 'email', 'quantity']
