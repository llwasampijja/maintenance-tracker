from rest_framework import status
from rest_framework.test import APITestCase
from django.contrib.auth.models import User

class UserTests(APITestCase):
    users_url = '/api/v1/users/'
    register_url = '/api/v1/auth/register/'
    def setUp(self):
        user_data = {'username': 'lauren', 'email':'lauren@bolon.com', 'password':'password#1'}
        self.client.post(self.register_url, user_data, format='json')
        user_data2 = {'username': 'test0', 'email':'test0@bolon.com', 'password':'password#1'}
        self.client.post(self.register_url, user_data2, format='json')
        self.client.login(username='lauren', password='password#1')

    def test_login_user(self):
        """
        Test if a user logs in successifully
        """
        response = self.client.login(username='lauren', password='password#1')
        self.assertTrue(response)

    def test_login_user_wrong_username(self):
        """
        Test if a user logs in with wrong username
        """
        response = self.client.login(username='laury', password='password#1')
        self.assertFalse(response)

    def test_login_user_wrong_password(self):
        """
        Test if a user logs in with wrong password
        """
        response = self.client.login(username='lauren', password='password#2')
        self.assertFalse(response)

    def test_register_user_success(self):
        """
        Test if a user a user registers successifully
        """
        data = {'username': 'test1', 'email':'test1@bolon.com', 'password':'password#1'}
        response = self.client.post(self.register_url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_register_user_username_exists(self):
        """
        Test if a user a user registers with existing username
        """
        data = {'username': 'test0', 'email':'test0@bolon.com', 'password':'password#1'}
        response = self.client.post(self.register_url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_register_user_email_exists(self):
        """
        Test if a user a user registers with existing email
        """
        data = {'username': 'test1', 'email':'test0@bolon.com', 'password':'password#1'}
        response = self.client.post(self.register_url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_register_user_no_username(self):
        """
        Test if a user a user registers without username
        """
        data = {'email':'test1@bolon.com', 'password':'password#1'}
        response = self.client.post(self.register_url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_register_user_no_email(self):
        """
        Test if a user a user registers without email
        """
        data = {'username': 'test1', 'password':'password#1'}
        response = self.client.post(self.register_url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_register_user_no_password(self):
        """
        Test if a user a user registers without password
        """
        data = {'username': 'test1', 'email':'test1@bolon.com'}
        response = self.client.post(self.register_url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_delete_user(self):
        """
        Test delete a user by id  successfully
        """
        user_url = self.users_url + '2/'
        response = self.client.delete(user_url, format='json')
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)

    def test_delete_user_not_exist(self):
        """
        Test delete a user by id  who doesnt exist
        """
        user_url = self.users_url + '3/'
        response = self.client.delete(user_url, format='json')
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)


    def test_get_users(self):
        """
        Test get users
        """
        response = self.client.get(self.users_url, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_get_user(self):
        """
        Test get a user by id successfully
        """
        user_url = self.users_url + '2/'
        response = self.client.get(user_url, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_get_user_not_exist(self):
        """
        Test get a user by id  who doesnt exist
        """
        user_url = self.users_url + '3/'
        response = self.client.get(user_url, format='json')
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)
