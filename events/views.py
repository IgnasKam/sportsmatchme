from django.contrib.auth.decorators import login_required
from django.shortcuts import render

# Create your views here.
def main_event_view(request):
    # Your view logic here
    return render(request, 'events/1events.html')

@login_required
def events_create(request):
    # Your code for events_create
    return render(request, 'events/create_event.html')

@login_required
def events_list(request):
    # Your code for events_list
    return render(request, 'events/list_event.html')

@login_required
def events_list_filter(request):
    # Your code for events_list_filter
    return render(request, 'events/list_filter_event.html')

