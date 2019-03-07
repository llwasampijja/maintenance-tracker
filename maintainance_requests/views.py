from django.shortcuts import render
from maintainance_requests.models import MaintainanceRequest
from maintainance_requests.serializers import MaintainanceRequestSerializer 
from rest_framework.viewsets import ModelViewSet
# from rest_framework.authentication import SessionAuthentication, BasicAuthentication, IsAuthenticated
# Create your views here.


# from django.shortcuts import render
# # from django.contrib.auth.models import User, Group
# from rest_framework.viewsets import ModelViewSet

# from rest_framework.decorators import action
# from rest_framework.response import Response
# from rest_framework import status

class MaintainanceRequestViewSet(ModelViewSet):
    """API Endpoint for viewing and editting user details"""
    queryset = MaintainanceRequest.objects.all().order_by('-date_posted')
    serializer_class = MaintainanceRequestSerializer
    # authentication_classes = (SessionAuthentication, BasicAuthentication)
    # permission_classes = (IsAuthenticated,)

    # def perform_create(self, serializer):
    #     serializer.save(author=self.request.user)
