from django.contrib.auth.models import User

from django.db import models
from courts.models import Court
from django.core.validators import MinValueValidator
from django.conf import settings
from django.contrib.auth.models import AbstractUser

class CustomUser(AbstractUser):

    class Meta:
        db_table='custom_user'
        swappable= 'AUTH_USER_MODEL'

    def __str__(self):
        return self.username

class Profile(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    height = models.IntegerField(validators=[MinValueValidator(0)], null=True, blank=True)
    weight = models.IntegerField(validators=[MinValueValidator(0)], null=True, blank=True)
    nationality = models.CharField(max_length=50)
    birth_date = models.DateField(null=True, blank=True)
    favorite_sport = models.CharField(max_length=30)
    favorite_team = models.CharField(max_length=50)
    favorite_player = models.CharField(max_length=50)
    bio = models.TextField(max_length=500, blank=True)
    picture = models.ImageField(upload_to='images/', null=True, blank=True)

    def __str__(self):
        return self.user

