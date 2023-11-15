from django.urls import path
from . import views

app_name = 'courts'

urlpatterns = [
    path('', views.main_court_view, name='main_court_view'),
    path('create/', views.create_court, name='court_create'),
    path('list/', views.court_list, name='court_list'),
]
