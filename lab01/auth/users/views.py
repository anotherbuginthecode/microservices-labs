from django.conf import settings
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.exceptions import AuthenticationFailed
import jwt

from .serializers import UserSerializer
from .models import User
from auth.decorators import jwt_required

# Create your views here.
class RegisterView(APIView):
    def post(self, request):
        serializer = UserSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)

class ListUserView(APIView):
    @jwt_required # only a valid token can access this view
    def get(self, request):
        users = User.objects.all()
        serializer = UserSerializer(users, many=True)

        return Response(serializer.data)

class SingleUserView(APIView):
    @jwt_required # only a valid token can access this view
    def get(self, request, id):
        user = User.objects.filter(id=id).first()
        if user:
            serializer = UserSerializer(user)
            return Response(serializer.data)
        
        return Response({'message': 'user not found.'}, status=404)

class MeView(APIView):
    @jwt_required # only a valid token can access this view
    def get(self, request):

        token = request.headers.get('Authorization').split('Bearer ')[1]
        try:
            payload = jwt.decode(token, settings.SECRET_KEY, algorithms="HS256")
        except jwt.ExpiredSignatureError:
            raise AuthenticationFailed('Unauthenticated')
        
        user = User.objects.filter(id=payload['user_id']).first()
        serializer = UserSerializer(user)
        return Response(serializer.data)