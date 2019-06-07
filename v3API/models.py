from django.db import models

# Create your models here.

class AuthModel(models.Model):
    authorization_token = models.CharField(max_length=100)
    refresh_token = models.CharField(max_length=100)
    last_used = models.DateTimeField(max_length=100)