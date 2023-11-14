from django.contrib.auth.models import User

from django.db import models
from django.conf import settings


class Court(models.Model):
    name = models.CharField(max_length=100, null=False, blank=True)
    owner = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.SET_NULL, null=True, related_name='owned_courts')
    address = models.CharField(max_length=255, null=False, blank=True)
    open_hours = models.TextField(max_length=255, null=False, blank=True)
    website = models.CharField(max_length=255, null=True, blank=True)
    phone = models.CharField(max_length=30, null=True, blank=True)
    email = models.EmailField(max_length=80, null=True, blank=True)
    pictures = models.ImageField(upload_to='images/', null=True, blank=True)


    def save(self, *args, **kwargs):
        if self._state.adding and not self.owner:
            pass
        super(Court, self).save(*args, **kwargs)

    def __str__(self):
        return self.name
