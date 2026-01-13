import requests
from utils.config import Config

class UserApi:
    def __init__(self):
        self.base_url = f"{Config.BASE_URL}/users"
        self.headers = {
            "Authorization": f"Bearer {Config.TOKEN}",
            "Content-Type": "application/json",
            "Accept": "application/json"
        }
    
    def create_user(self, payload):
        return requests.post(self.base_url, json=payload, headers=self.headers)
    
    def get_user(self, user_id):
        url = f"{self.base_url}/{user_id}"
        return requests.get(url, headers=self.headers)
    
    def delete_user(self, user_id):
        url = f"{self.base_url}/{user_id}"
        return requests.delete(url, headers=self.headers)
    
