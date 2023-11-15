from django.urls import path
from . import views

app_name = 'events'

urlpatterns = [
    path('', views.main_event_view, name='main_event_view'),  # An example user profile URL
    path('create/', views.events_create, name='events_create'),
    path('list/', views.events_list, name='events_list'),

]
