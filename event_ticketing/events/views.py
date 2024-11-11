from django.shortcuts import render, get_object_or_404, redirect
from .models import Event, Ticket
from .forms import EventForm, TicketForm

def event_list(request):
    events = Event.objects.all()
    return render(request, 'events/event_list.html', {'events': events})

def event_detail(request, pk):
    event = get_object_or_404(Event, pk=pk)
    return render(request, 'events/event_detail.html', {'event': event})

def create_event(request):
    if request.method == "POST":
        form = EventForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('event_list')
    else:
        form = EventForm()
    return render(request, 'events/event_form.html', {'form': form})

def book_ticket(request, pk):
    event = get_object_or_404(Event, pk=pk)
    if request.method == "POST":
        form = TicketForm(request.POST)
        if form.is_valid():
            ticket = form.save(commit=False)
            ticket.event = event
            ticket.save()
            return redirect('event_detail', pk=event.pk)
    else:
        form = TicketForm()
    return render(request, 'events/book_ticket.html', {'form': form, 'event': event})
