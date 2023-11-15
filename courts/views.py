from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from .forms import CourtForm
from .models import Court


@login_required  # Ensure that only logged-in users can create a court
def create_court(request):
    if request.method == 'POST':
        form = CourtForm(request.POST,
                         request.FILES)  # Pass in request.FILES if your form includes file upload like images
        if form.is_valid():
            court = form.save(commit=False)  # Create Court instance but don't save to DB yet
            court.owner = request.user  # Set the current user as the owner
            court.save()  # Save Court instance to DB with owner
            return HttpResponseRedirect(reverse('courts:main_court_view'))  # Redirect to court's main view after saving
    else:
        form = CourtForm()

    return render(request, 'courts/create_court.html', {'form': form})

@login_required
def main_court_view(request):
    return render(request, 'courts/1courts.html')

@login_required
def court_list(request):
    courts = Court.objects.all()  # Fetch all courts initially

    # Implementing Search
    search_query = request.GET.get('search', '')
    if search_query:
        courts = courts.filter(name__icontains=search_query)

    # Implementing Sorting (example: sorting by name)
    sort_by = request.GET.get('sort', 'name')
    courts = courts.order_by(sort_by)

    return render(request, 'courts/list_court.html', {'courts': courts, 'search_query': search_query})