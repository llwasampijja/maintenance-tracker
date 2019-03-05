from django.shortcuts import render
from django.contrib.auth.models import User, Group
from rest_framework.viewsets import ModelViewSet
from auth.serializers import UserSerializer, GroupSerializer

class UserViewSet(ModelViewSet):
    """API Endpoint for viewing and editting user details"""
    queryset = User.objects.all().order_by('-date_joined')
    serializer_class = UserSerializer


class GroupViewSet(ModelViewSet):
    """API Endpoint for viewing and editting group details"""
    queryset = Group.objects.all()
    serializer_class = GroupSerializer