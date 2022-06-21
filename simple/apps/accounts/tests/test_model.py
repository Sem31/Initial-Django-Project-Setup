from django.test import TestCase
from simple.apps.accounts.models import User

class UserTestCase(TestCase):

    @classmethod
    def setUpTestData(cls) -> None:
        cls.username = "sem31"
        cls.email = "sem31@gmail.com"
        cls.password = "sem12345.."

    def setUp(self) -> None:
        print("Test User DB")

    def tearDown(self) -> None:
        user = User.objects.get(email=self.email)
        user.delete()


    def test_create_user(self) -> None:
        user = User.objects.create(
            email=self.email
        )
        user.set_password(self.password)
        user.save()

        self.assertTrue(isinstance(user, User))
        assert user.email == self.email
