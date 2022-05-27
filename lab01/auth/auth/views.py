import jwt
from django.conf import settings
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.exceptions import AuthenticationFailed


from .decorators import jwt_required

class TokenDecode(APIView):
    @jwt_required # only a valid token can access this view
    def post(self, request):
        token = request.data.get('token', None)
        if token:
            try:
                payload = jwt.decode(token, settings.SECRET_KEY, algorithms="HS256")
            except jwt.ExpiredSignatureError:
                raise AuthenticationFailed('Unauthenticated')

            return Response({'id': payload['user_id']})
        
        raise AuthenticationFailed('Unauthenticated')
