import urllib
import requests as r
import os

from v3API.models import AuthModel

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
        return redirect(base_url+params)

    @staticmethod
    def store_new_tokens(response:r.Response):
        json_data = request.json()
        access_token = json_data['access_toekn']
        refresh_token = json_data['refresh_token']

        new_token = AuthModel(authorization_token=access_token, refresh_token=refresh_token)
        new_token.save()
        
        return(new_token['authorization_token'], new_token['refresh_token'])


    @staticmethod
    def get_tokens(code):
        base_url = "https://idfed.constantcontact.com/as/token.oauth2?"
        data = {
            "code":code,
            "redirect_uri":"http://localhost:8000",
            "grant_type":"authorization_code",
        }
        auth_headers = (os.environ['V3APIKEY'], os.environ['V3APISECRET'])

        response = r.post(base_url, data=data, auth=auth_headers)
        store_new_tokens(response)

        return r.post(base_url, data=data, auth=auth_headers)
    
    @staticmethod
    def check_token_expiration():
        pass

    @staticmethod
    def refresh_token(refresh_token):
        base_url = "https://idfed.constantcontact.com/as/token.oauth2?"
        data = {
            "refresh_token": refresh_token,
            "grant_type":"refresh_token",
                    }
        auth_headers = (os.environ['V3APIKEY'], os.environ['V3APISECRET'])

        response = r.post(base_url, data=data, auth=auth_headers)
        

class CTCTContactAPIs():

    @staticmethod
    # NOTE: Can I just use (email, *, **kwargs) here to include ANY info given to function? 
    def add_contact(first_name, email_address):
            # If you add additional fields to the jmml form, you will need to update this method 
            # and the form_valid medthod on the SignUpView view to include those fields
        
        params = {
            "first_name": first_name,
            "email_address": email_address,
        }

        base_url = "https://api.cc.email/v3/contacts"
        # GET to verify if contact already exists:
        contact_exists = _check_contact_exists(email_address)
        # PUT if contact already exists
        if contact_exists: 
            _update_existing_contact()
        # POST if contact doesn't exist yet
        else:
            _send_new_contact() request = r.post()
    
    @staticmethod
    def _check_contact_exists(email_address):
        #GET
        pass

    @staticmethod
    def _send_new_contact(email_address, *, **kwargs):
        #POST
        pass
    
    @staticmethod
    #PUT
    def _update_existing_contact(email_address, *, **kwargs):
        pass