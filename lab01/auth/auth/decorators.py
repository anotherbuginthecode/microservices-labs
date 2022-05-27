from functools import wraps
from rest_framework.exceptions import AuthenticationFailed


def jwt_required(function):
    @wraps(function)
    def decorator(*args, **kwargs):
        token = args[0].request.headers.get('Authorization', None)
        if not token:
            raise AuthenticationFailed('Unauthenitcated')

        return function(*args, **kwargs)

    return decorator