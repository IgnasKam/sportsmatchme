from django.shortcuts import render

# Create your views here.
def maineventsview(request):
    # Your view logic here
    return render(request, 'events/1events.html')