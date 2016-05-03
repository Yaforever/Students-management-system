from django.test import TestCase


class Auth_Test(TestCase):

    def test_auth_login(self):
        response = self.client.post('/', {'username': 'admin', 'password': '5t5t5t5t'})
        self.assertEqual(response.status_code, 200) 

    def test_auth_email(self):
        response = self.client.post('/', {'username': 'lasthoprofyou@gmail.com', 'password': '5t5t5t5t'})
        self.assertEqual(response.status_code, 200) 




