from django.shortcuts import render

# Create your views here.
def profile(request):
    # Your view logic here
    return render(request, 'users/profile.html')