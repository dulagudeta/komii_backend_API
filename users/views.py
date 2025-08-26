from django.shortcuts import render
from rest_framework import generics
from django.contrib.auth import get_user_model
from .serializers import RegisterSerializer, UserSerializer
from rest_framework.permissions import AllowAny

User = get_user_model()

class RegisterView(generics.CreateAPIView):
    queryset = User.objects.all()
    permission_classes = [AllowAny]  # Anyone can register
    serializer_class = RegisterSerializer
class UserListView(generics.ListAPIView):
    queryset = User.objects.all()
    permission_classes = [AllowAny]  # Adjust permissions as needed
    serializer_class = UserSerializer


