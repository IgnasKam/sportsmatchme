from django import forms
from .models import Event

class EventForm(forms.ModelForm):
    class Meta:
        model = Event
        fields = ['name', 'event_date', 'location', 'court', 'duration',
                  'player_limit', 'teams_limit', 'players', 'logo',
                  'public_or_private', 'description']