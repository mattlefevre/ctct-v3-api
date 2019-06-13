from django.db import models
from v3API.services import CTCTAuth

# Create your models here.

class AuthModel(models.Model):
    authorization_token = models.CharField(max_length=100)
    refresh_token = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)
    last_used = models.DateTimeField(auto_now=True)


#NOTE: Need to figure out how to get row 1, token
def get_auth_token():
    query = AuthModel.objects.filter(id=1)
    print(f"Getting Authorization Token: {query['authorization_token']}")
    return query['authorization_token']

def get_refresh_token():
    query = AuthModel.objects.filter(id=1)
    print(f"Getting Refresh Token: {query['refresh_token']}")
    return query['refresh_token']