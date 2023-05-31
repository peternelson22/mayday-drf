from urllib.request import Request
from django.shortcuts import get_object_or_404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework.authentication import SessionAuthentication, TokenAuthentication
from rest_framework import status
from rest_framework.authtoken.models import Token
from django.contrib.auth.models import User
from .serializers import UserSerializer


class Login(APIView):
    permission_classes = []
    authentication_classes = []
    def post(self, request: Request):
        user = get_object_or_404(User, username=request.data.get('username'))
        if not user.check_password(request.data.get('password')):
            return Response({"detail": "Not Found"}, status=status.HTTP_404_NOT_FOUND)
        token, created = Token.objects.get_or_create(user=user)
        serializer = UserSerializer(instance=user)
        return Response({"token": token.key, "data": serializer.data})


class SignUp(APIView):
    permission_classes = []
    authentication_classes = []
    def post(self, request: Request):
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            user = User.objects.get(username=request.data.get('username'))
            user.set_password(request.data.get('password'))
            user.save()
            token = Token.objects.create(user=user)
            return Response({"token": token.key, "user": serializer.data})
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class TestToken(APIView):
    permission_classes = [IsAuthenticated]
    authentication_classes = [SessionAuthentication, TokenAuthentication]
    def get(self, request: Request):
        return Response("passed for {}".format(request.user.email))
