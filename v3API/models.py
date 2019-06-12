from django.db import models

# Create your models here.

class AuthModel(models.Model):
    authorization_token = models.CharField(max_length=100)
    refresh_token = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)
    last_used = models.DateTimeField(auto_now=True)

def get_most_recent():
    query = AuthModel.objects.filter(id=1)
