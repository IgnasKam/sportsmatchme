from django.contrib.auth.decorators import login_required
from django.http import HttpResponseForbidden
from django.shortcuts import render, redirect, get_object_or_404
from .forms import EventForm
from users.models import Profile
from .models import Event


# Create your views here.
def main_event_view(request):
    # Your view logic here
    return render(request, 'events/1events.html')

@login_required
def events_create(request):
    if request.method == 'POST':
        form = EventForm(request.POST, request.FILES)
        if form.is_valid():
            event = form.save(commit=False)
            event.host = request.user.profile
            event.save()
            form.save_m2m()
            return redirect('events:events_list')
    else:
        form = EventForm()
    return render(request, 'events/create_event.html', {'form': form})

@login_required
def events_list(request):
    events = Event.objects.all()
    return render(request, 'events/list_event.html', {'events': events})

@login_required
def events_list_filter(request):
    query_date = request.GET.get('date')
    query_location = request.GET.get('location')
    events = Event.objects.all()

    if query_date:
        events = events.filter(event_date__date=query_date)
    if query_location:
        events = events.filter(location__icontains=query_location)

    return render(request, 'events/list_filter_event.html', {'events': events})
@login_required
def events_edit(request, event_id):
    event = get_object_or_404(Event, id=event_id)

    if request.user.profile != event.host and not request.user.is_staff:
        return HttpResponseForbidden()