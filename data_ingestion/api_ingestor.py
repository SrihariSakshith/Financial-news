import requests

def fetch_api_data(api_url, headers=None):
    response = requests.get(api_url, headers=headers)
    if response.status_code == 200:
        return response.json()
    else:
        response.raise_for_status()
