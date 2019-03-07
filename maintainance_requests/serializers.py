from maintainance_requests.models import MaintainanceRequest
from rest_framework.serializers import HyperlinkedModelSerializer, PrimaryKeyRelatedField, CurrentUserDefault
from rest_framework import serializers


class MaintainanceRequestSerializer(HyperlinkedModelSerializer):
    author = PrimaryKeyRelatedField(read_only=True, default=serializers.CurrentUserDefault())
    print("current epur op: ", CurrentUserDefault())
    class Meta:
        model = MaintainanceRequest
        fields = ('url', 'request_title', 'request_description', 'date_posted', 'author')
        # fields = ('url', 'request_title', 'request_description', 'date_posted')
        