from django.shortcuts import render, redirect
from .forms import CustomUserCreationForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin


# Create your views here.
def user_profile_view(request):
    # Your view logic here
    return render(request, 'users/profile.html')

def register(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')  # Redirect to login page after registration
    else:
        form = CustomUserCreationForm()
    return render(request, 'users/register.html', {'form': form})



# @login_required
# def some_view(request):
#
#     # Your view logic
# class SomeProtectedView(LoginRequiredMixin, View):
#     # Your view logic here
#     pass