from django.urls import path
from . import views

urlpatterns = [
    path('', views.maineventsview, name='main_event_view'),  # An example user profile URL
    # ... other user-related URLs ...
]
