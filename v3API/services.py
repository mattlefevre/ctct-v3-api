import urllib
import requests as r
import os

class CTCTAuth():
    """
    Holds all methods relating to authenticating to Constant Contact's API
    """

    @staticmethod
    def get_authorization():
        params = {
            "client_id": os.environ.get('V3APIKEY'),
            "scope":"contact_data+campaign_data",
            "response_type":"code",
            "redirect_uri": "http://localhost:8000",
        }
        # Manually encode params, since we're returning a redirectable URL, not a GET request
        params = urllib.parse.urlencode(params,safe="+")
        base_url = "https://api.cc.email/v3/idfed?"
        return base_url+params

    @staticmethod
    def get_tokens(code):
        base_url = "https://idfed.constantcontact.com/as/token.oauth2?"
        data = {
            "code":code,
            "redirect_uri":"http://localhost:8000",
            "grant_type":"authorization_code",
        }
        headers = (os.environ['V3APIKEY'], os.environ['V3APISECRET'])

        return r.post(base_url, data=data, auth=headers)
    
    @staticmethod
    def check_token_expiration():
        pass

    @staticmethod
    def refresh_token():
        pass


def send_contact(first_name, email_address):
        # If you add additional fields to the jmml form, you will need to update this method 
        # and the form_valid medthod on the SignUpView view to include those fields
    params = {
        "first_name": first_name,
        "email_address": email_address,
    }

    base_url = "https://api.cc.email/v3/contacts"
    # GET to verify if contact already exists:

    # POST if contact doesn't already exist
    request = r.post()
