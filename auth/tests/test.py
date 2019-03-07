from rest_framework import status
from rest_framework.test import APITestCase

class UserTests(APITestCase):
    def test_register_user(self):
        """
        Make sure a user registers successifully
        """
        url = '/api/v1/auth/register/'
        data = {'username': 'test0', 'email':'test0@bolon.com', 'password':'password#1'}
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_delete_user(self):
        """
        Make sure a user registers successifully
        """
        url = '/api/v1/users/2/'
        data = {'username': 'test0', 'email':'test0@bolon.com', 'password':'password#1'}
        self.client.post(url, data, format='json')
        response = self.client.delete(url, data, format='json')
        # self.assertEqual(response.status_code, status.HTTP_200_OK)


    def test_get_users(self):
        """
        Make sure a user registers successifully
        """
        url = '/api/v1/users/'
        data = {'username': 'test0', 'email':'test0@bolon.com', 'password':'password#1'}
        self.client.post(url, data, format='json')
        response = self.client.get(url, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_get_user(self):
        """
        Make sure a user registers successifully
        """
        url = '/api/v1/users/1/'
        data = {'username': 'test0', 'email':'test0@bolon.com', 'password':'password#1'}
        self.client.post(url, data, format='json')
        response = self.client.get(url, format='json')
        # self.assertEqual(response.status_code, status.HTTP_200_OK)
