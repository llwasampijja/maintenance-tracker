from django.shortcuts import render
from django.contrib.auth.models import User, Group
from rest_framework.viewsets import ModelViewSet
from auth.serializers import UserSerializer, GroupSerializer 
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework import status

class UserViewSet(ModelViewSet):
    """API Endpoint for viewing and editting user details"""
    queryset = User.objects.all().order_by('-date_joined')
    serializer_class = UserSerializer
    http_method_names = ['put', 'patch', 'get', 'delete']

class GroupViewSet(ModelViewSet):
    """API Endpoint for viewing and editting group details"""
    queryset = Group.objects.all()
    serializer_class = GroupSerializer

class UserRegisterViewSet(ModelViewSet):
    queryset = User.objects.all().order_by('-date_joined')
    serializer_class = UserSerializer
    http_method_names = ['post']
