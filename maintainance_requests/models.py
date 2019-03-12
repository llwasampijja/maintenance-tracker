from django.db import models


from django.utils import timezone
from django.contrib.auth.models import User
from django.urls import reverse
from rest_framework.serializers import HyperlinkedModelSerializer, PrimaryKeyRelatedField, CurrentUserDefault


class MaintainanceRequest(models.Model):
    author = PrimaryKeyRelatedField(read_only=True, default=CurrentUserDefault())
    request_title = models.CharField(max_length=100)
    request_description = models.TextField()
    date_posted = models.DateTimeField(default=timezone.now)
    author = models.ForeignKey(User, on_delete=models.CASCADE, null=True)


    def __str__(self):
        return self.request_title

    def get_absolute_url(self):
        return reverse('post-detail', kwargs={'pk': self.pk})