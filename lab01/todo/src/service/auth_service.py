import requests
import json
import os
from flask import abort

class Auth():
    def __init__(self):
        self.AUTH_SERVICE_NAME = os.getenv('AUTH_SERVICE_NAME', 'localhost')
        self.AUTH_SERVICE_PORT = os.getenv('AUTH_SERVICE_PORT', '8000')
    
    def is_authorized(self, token):
        BASE_URL = f'http://{self.AUTH_SERVICE_NAME}:{self.AUTH_SERVICE_PORT}/api/v1/auth/token/verify/'
        res = requests.post(BASE_URL, data={'token': token})
        if (res.status_code) // 100 == 2:
            return True
        return False
    
    def get_user(self, token):
        BASE_URL = f'http://{self.AUTH_SERVICE_NAME}:{self.AUTH_SERVICE_PORT}/api/v1/auth/token/decode/'
        headers = {
            'Authorization': 'Bearer {}'.format(token),
        }
        res = requests.post(BASE_URL, data={'token': token}, headers=headers)
        if (res.status_code) // 100 == 2:
            return json.loads(res.text)
        return abort(404)