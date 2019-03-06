from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase

class AccountTests(APITestCase):
    def test_register_user(self):
        """
        Ensure we can create a new account object.
        """
        url = '/api/v1/auth/register/'
        data = {'username': 'test0', 'email':'test0@bolon.com', 'password':'password#1'}
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)