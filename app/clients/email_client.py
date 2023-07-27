import requests
from typing import Any


class EmailClient:
    def __init__(self, base_url):
        self.BASE_URL = base_url

    def send_registration_email(self, email_address: str) -> Any:
        url = self.BASE_URL + '/welcome-email'
        body = {'address': email_address}
        try:
            response = requests.post(url, json=body)
            if response.status_code == 200:
                return response.json()
            else:
                return None
        except:
            return None
