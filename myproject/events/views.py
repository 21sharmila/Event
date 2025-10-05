# Create your views here.
from django.shortcuts import render, redirect, get_object_or_404
from django.db.models import Q
from .models import Event
from .forms import EventForm

# Home
def home(request):
    return render(request, 'home.html')

# display
def event_list(request):
    query = request.GET.get('q')
    if query:
        events = Event.objects.filter( 
            Q(title__icontains=query) | Q(date__icontains=query)
        )
    else:
        events = Event.objects.all().order_by('date', 'time')
    return render(request, 'display.html', {'events': events})

# Add Event
def add_event(request):
    if request.method == "POST":
        form = EventForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('event_list')
    else:
        form = EventForm()
    return render(request, 'add.html', {'form': form})

# Update Event
def update_event(request, pk):
    event = get_object_or_404(Event, pk=pk)
    if request.method == "POST":
        form = EventForm(request.POST, instance=event)
        if form.is_valid():
            form.save()
            return redirect('event_list')
    else:
        form = EventForm(instance=event)
    return render(request, 'update.html', {'form': form})

# Delete Event
def delete_event(request, pk):
    event = get_object_or_404(Event, pk=pk)
    if request.method == "POST":
        event.delete()
        return redirect('event_list')
    return render(request, 'delete.html', {'event': event})
