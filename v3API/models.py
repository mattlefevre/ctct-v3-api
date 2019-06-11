from django.db import models

# Create your models here.

class AuthManager(models.Manager):
    def most_recent(self):
        return self.filter()

class AuthModel(models.Model):
    authorization_token = models.CharField(max_length=100)
    refresh_token = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)
    last_used = models.DateTimeField(auto_now=True)
    objects = AuthManager()


