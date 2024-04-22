from rest_framework.views import APIView
from rest_framework import status
from rest_framework.response import Response
from .serializers import user_register_serializer, user_login_serializer
from django.contrib.auth import authenticate
from django.contrib.auth.models import User
from rest_framework.authtoken.models import Token
from rest_framework.permissions import IsAuthenticated
from rest_framework.authentication import TokenAuthentication

class user_register_api(APIView):
    def post(self, request):
        data = request.data
        serializer = user_register_serializer(data=data)
        if not serializer.is_valid():
            return Response({
                "status" : False,
                "message" : serializer.errors
            }, status=status.HTTP_400_BAD_REQUEST)
        serializer.save()
        return Response({
            "status" : True,
            "message" : "User Created Successfully"
        }, status=status.HTTP_200_OK)
    
class user_login_api(APIView):
    def post(self, request):
        data = request.data
        serializer = user_login_serializer(data=data)
        if not serializer.is_valid():
            return Response({
                "status" : False,
                "message" : serializer.errors
            }, status=status.HTTP_400_BAD_REQUEST)
        user = serializer.validated_data
        user = authenticate(username=user['username'], password=user['password'])
        if user:
            token, flag = Token.objects.get_or_create(user=user)
            return Response({
                "status" : True,
                "token" : str(token)
            })
        return Response({
            "status" : False,
            "message" : "Invalid credentials"
        }, status=status.HTTP_400_BAD_REQUEST)
    
class authenticated_check_API(APIView):
    permission_classes = [IsAuthenticated]
    authentication_classes = [TokenAuthentication]

    def get(self, request):
        return Response("User is authenticated.")
