from django.contrib import admin

# Register your models here.
from .models import Profile

# Replace 'Profile', 'Event', 'Court' with your model names
admin.site.register(Profile)
