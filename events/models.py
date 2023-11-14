from django.db import models
from django.contrib.auth.models import User
from users.models import Profile
from courts.models import Court


# Create your models here.
class Event(models.Model):
    name = models.CharField(max_length=100)
    host = models.ForeignKey(Profile, on_delete=models.CASCADE, related_name='hosted_events')
    event_date = models.DateTimeField()
    location = models.CharField(max_length=100)
    court = models.ForeignKey(Court, on_delete=models.SET_NULL, null=True, related_name='events')
    duration = models.DurationField(null=True, blank=True)
    player_limit = models.IntegerField(null=True, blank=True)
    teams_limit = models.IntegerField(null=True, blank=True)
    players = models.ManyToManyField(Profile, related_name='events')
    logo = models.ImageField(upload_to='images/',null=True, blank=True)
    public_or_private = models.BooleanField(default=True)
    description = models.TextField(max_length=500, blank=True)

    def __str__(self):
        return self.name
