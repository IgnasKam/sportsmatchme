from django.contrib.auth.models import User

from django.db import models
from courts.models import Court
from django.core.validators import MinValueValidator
from django.conf import settings



class Profile(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    height = models.IntegerField(validators=[MinValueValidator(0)], null=True, blank=True)
    weight = models.IntegerField(validators=[MinValueValidator(0)], null=True, blank=True)
    nationality = models.CharField(max_length=50)
    favorite_court = models.ForeignKey('courts.Court', on_delete=models.SET_NULL, null=True, blank=True, related_name='favored_by_profiles')
    birth_date = models.DateField(null=True, blank=True)
    favorite_sport = models.CharField(max_length=30)
    favorite_team = models.CharField(max_length=50)
    favorite_player = models.CharField(max_length=50)
    bio = models.TextField(max_length=500, blank=True)
    picture = models.ImageField(upload_to='images/', null=True, blank=True)
    friends = models.ManyToManyField('self', blank=True)

    def __str__(self):
        return self.user
