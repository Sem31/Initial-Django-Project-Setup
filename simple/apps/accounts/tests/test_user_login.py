from django.test import TestCase
from django.urls import reverse

from rest_framework import status


class UserLoginTest(TestCase):

    @classmethod
    def setUpTestData(cls) -> None:
        cls.payload = {
            "email": "kamlesh@gmail.com",
            "password": "Kamlesh12345..",
            "profile": {
                "first_name": "sem",
                "last_name": "prajapat",
                "phone_number": "1234567890",
                "age": 24,
                "gender": "M"
            }
        }

    def setUp(self) -> None:
        self.client.post(reverse("user_signup"), self.payload, 'application/json')
        print("Test started")

    def tearDown(self) -> None:
        print("Test ended")

    def test_user_login(self) -> None:
        payload = {
            "email": "kamlesh@gmail.com",
            "password": "Kamlesh12345..",
        }
        response = self.client.post(reverse("user_signin"), payload, 'application/json')
        data = response.json()
        self.assertEqual(status.HTTP_200_OK, response.status_code)
        self.assertEqual(data.get('message', None), "User logged in  successfully")
    
    def test_user_login_with_invalid_cred(self) -> None:
        payload = {
            "email": "kamlesh@gmail.com",
            "password": "Kamlesh12345",
        }
        response = self.client.post(reverse("user_signin"), payload, 'application/json')
        data = response.json()
        self.assertEqual(status.HTTP_400_BAD_REQUEST, response.status_code)
        self.assertEqual(data.get('non_field_errors', None)[0], "A user with this email and password is not found.")
