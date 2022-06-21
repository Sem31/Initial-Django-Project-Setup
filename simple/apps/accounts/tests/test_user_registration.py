from django.test import TestCase
from django.urls import reverse

from rest_framework import status


class UserRegistrationTest(TestCase):
    def test_user_registration(self) -> None:
        payload = {
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
        response = self.client.post(reverse("user_signup"), payload, 'application/json')
        data = response.json()
        self.assertEqual(status.HTTP_201_CREATED, response.status_code)
        self.assertEqual(data.get('message', None), "User registered  successfully")

    def test_user_registration_with_already_exists_email(self) -> None:
        payload = {
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
        response = self.client.post(reverse("user_signup"), payload, 'application/json')
        response = self.client.post(reverse("user_signup"), payload, 'application/json')
        data = response.json()
        self.assertEqual(status.HTTP_400_BAD_REQUEST, response.status_code)
        self.assertEqual(data.get('email')[0], "user with this email address already exists.")
