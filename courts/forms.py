# courts/forms.py
from django import forms
from .models import Court
class CourtForm(forms.ModelForm):
    class Meta:
        model = Court
        fields = ['name', 'address', 'open_hours', 'phone', 'email', 'website', 'pictures']  # List all fields except 'owner' which will be set to the current user
        # widgets = {
        #     'name': forms.TextInput(attrs={'class': 'form-control'}),
        #     'address': forms.TextInput(attrs={'class': 'form-control'}),
        #     'open_hours': forms.TextInput(attrs={'class': 'form-control'}),
        #     'phone': forms.TextInput(attrs={'class': 'form-control'}),
        #     'email': forms.TextInput(attrs={'class': 'form-control'}),
        #     'website': forms.TextInput(attrs={'class': 'form-control'}),
        #     'pictures': forms.FileInput(attrs={'class': 'form-control'}),
        # }
