from django.contrib.auth.models import User
from rest_framework.serializers import HyperlinkedModelSerializer, PrimaryKeyRelatedField
from rest_framework.validators import UniqueValidator
from maintainance_requests.models import MaintainanceRequest

class UserSerializer(HyperlinkedModelSerializer):
    # requests = PrimaryKeyRelatedField(many=True, queryset=MaintainanceRequest.objects.all())
    class Meta:
        model = User
        fields = ('url', 'username', 'email', 'password', 'first_name', 'last_name', 'date_joined')
        extra_kwargs = {'email': {'allow_blank': False, 'required': True, 'validators':[UniqueValidator(queryset=User.objects.all())]}}
        