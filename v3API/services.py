import urllib
import requests
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
        return base_url+params

    @classmethod
    def store_new_tokens(cls,response:requests.Response):
        json_data = response.json()
        print(f"store_new_tokens: json_data variable: {json_data}")
        access_token = json_data['access_token']
        refresh_token = json_data['refresh_token']

        stored_token = cls.objects.get(id=1)
        stored_token.access_token = access_token
        stored_token.refresh_token = refresh_token
        stored_token.save()
        
        return(stored_token['authorization_token'], stored_token['refresh_token'])


    @staticmethod
    def get_tokens(code):
        base_url = "https://idfed.constantcontact.com/as/token.oauth2?"
        data = {
            "code":code,
            "redirect_uri":"http://localhost:8000",
            "grant_type":"authorization_code",
        }
        auth_headers = (os.environ['V3APIKEY'], os.environ['V3APISECRET'])

        response = requests.post(base_url, data=data, auth=auth_headers)
        if response.status_code == "400":
        # Save Tokens to database
            stored_tokens = CTCTAuth.store_new_tokens(response)
        else:
            stored_tokens = response
        return stored_tokens
    
    @staticmethod
    def check_token_expiration():
        pass

    @staticmethod
    def refresh_auth_token(refresh_token):
        base_url = "https://idfed.constantcontact.com/as/token.oauth2?"
        data = {
            "refresh_token": refresh_token,
            "grant_type":"refresh_token",
                    }
        auth_headers = (os.environ['V3APIKEY'], os.environ['V3APISECRET'])

        response = requests.post(base_url, data=data, auth=auth_headers)
        

class CTCTContactAPIs():

    @classmethod
    # NOTE: Can I just use (email, *, **kwargs) here to include ANY info given to function? 
    def add_contact(cls,first_name, email_address):
            # If you add additional fields to the jmml form, you will need to update this method 
            # and the form_valid medthod on the SignUpView view to include those fields
        
        params = {
            "first_name": first_name,
            "email_address": email_address,
        }

        base_url = "https://api.cc.email/v3/contacts"
        # GET to verify if contact already exists:
        contact_exists = cls._check_contact_exists(email_address)
        print(f"CTCTContactAPI: add_contacts: contact_exists variable: {contact_exists}")
        # PUT if contact already exists
        if contact_exists: 
            cls._update_existing_contact(email_address)
        # POST if contact doesn't exist yet
        else:
            passf
            _add_new_contact()
    
    @staticmethod
    def _check_contact_exists(email_address):
        #GET
        base_url = "https://api.cc.email/v3/contacts?email=new_contact_email"
        params = {
            "email":email_address,
        }
        headers = {
            "Authorization": f"Bearer {AuthModel.get_current_token}"
        }
        response = requests.get(base_url,params,auth=auth_headers)
        print(f"_check_contact_exists: response.status_code: {response.status_code}")
        return response.status_code

    @staticmethod
    def _add_new_contact(email_address, **kwargs):
        #NOTE: Depending on simplicity of function, this may be unnecessary abstraction
        #POST
        pass
    
    @staticmethod
    
    def _update_existing_contact(email_address, **kwargs):
        #NOTE: Depending on simplicity of function, this may be unnecessary abstraction
        #PUT
        pass