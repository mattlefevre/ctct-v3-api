from django.db import models

# Create your models here.

class AuthModel(models.Model):
    authorization_token = models.CharField()
    refresh_token = models.CharField()
    last_used = models.DateTimeField()