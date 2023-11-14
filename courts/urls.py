from django.urls import path
from . import views

urlpatterns = [
    path('', views.main_courtview, name='main_courtview'),
]
