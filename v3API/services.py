import urllib
import requests as r
import os

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

def get_tokens(code):
    base_url = "https://idfed.constantcontact.com/as/token.oauth2?"
    data = {
        "code":code,
        "redirect_uri":"http://localhost:8000",
        "grant_type":"authorization_code",
    }
    headers = (os.environ['V3APIKEY'], os.environ['V3APISECRET'])

    return r.post(base_url, data=data, auth=headers)



if __name__ == "__main__":
    # Just for testing
    client_id = os.environ.get('V3APIKEY')
    response = get_tokens("6ncJQYbVTX5hxPXh2FZWZxIH0hIXhBFAbaV3lADJ",redirect_uri)
    print(response.status_code)
    print()
    print(response.json())