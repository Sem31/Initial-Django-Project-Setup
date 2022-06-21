from django.test import TestCase
from django.urls import reverse

from rest_framework import status


class UserProfileTest(TestCase):
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
                "gender": "M",
            },
        }

    def setUp(self) -> None:
        self.client.post(reverse("user_signup"), self.payload, "application/json")
        print("Test started")

    def tearDown(self) -> None:
        print("Test ended")

    def test_get_user_profile(self) -> None:
        payload = {
            "email": "kamlesh@gmail.com",
            "password": "Kamlesh12345..",
        }
        response = self.client.post(reverse("user_signin"), payload, "application/json")
        data = response.json()
        self.client.defaults['HTTP_AUTHORIZATION'] = 'Bearer ' + data.get('token')
        response = self.client.get(reverse("get_user_profile"))
        data = response.json()
        self.assertEqual(status.HTTP_200_OK, response.status_code)
        self.assertEqual(data.get("message", None), "User profile fetched successfully")
