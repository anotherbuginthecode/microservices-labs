from functools import wraps
from flask import request, abort
from src.service.auth_service import Auth



def is_authorized(function):
    @wraps(function)
    def decorator(*args, **kwargs):
        token = request.headers.get('Authorization', None)
        if not token:
            return abort(401)
    
        headers = request.headers
        bearer = headers.get('Authorization') 
        token = bearer.split()[1]

        if Auth().is_authorized(token=token):
            return function(*args, **kwargs)
        return abort(401)

    return decorator