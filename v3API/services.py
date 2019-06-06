import requests
import os

def get_authorization(redirect_uri, client_id):
    params = {
        "redirect_uri": redirect_uri,
        "client_id":client_id,
        "scope":"contact_data",
        "respones_type":"code",
    }
    base_url = "https://api.cc.email/v3/idfed"
    
    return requests.get(base_url,params=params)


if __name__ == "__main__":
    redirect_uri = "localhost:8000/jmml"
    client_id = os.environ.get('V3APIKEY')
    print(get_authorization(redirect_uri, client_id))