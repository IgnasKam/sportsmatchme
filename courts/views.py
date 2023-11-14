from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from .forms import CourtForm  # Assuming you have a form for Court model

@login_required  # Ensure that only logged-in users can create a court
def create_court(request):
    if request.method == 'POST':
        form = CourtForm(request.POST, request.FILES)  # Pass in request.FILES if your form includes file upload like images
        if form.is_valid():
            court = form.save(commit=False)  # Create Court instance but don't save to DB yet
            court.owner = request.user  # Set the current user as the owner
            court.save()  # Save Court instance to DB with owner
            return HttpResponseRedirect(reverse('courts:main_court_view'))  # Redirect to court's main view after saving
    else:
        form = CourtForm()

    return render(request, 'courts/create_court.html', {'form': form})

def main_courtview(request):
    # Your view logic here
    return render(request, 'courts/1courts.html')
