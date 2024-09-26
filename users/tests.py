from django.test import TestCase
from users.models import User
from .models import Realtor

class RealtorModelTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        # Create a User instance for testing
        user = User.objects.create_user( email='test@example.com', password='password')

        # Create a Realtor instance
        realtor = Realtor.objects.create(user=user, profile='Test profile', agency='Test agency', city='Test city')

    def test_realtor_str_method(self):
        realtor = Realtor.objects.get(pk=1)  # Get the Realtor instance from the database
        expected_str = realtor.user.email
        self.assertEqual(str(realtor), expected_str)

# Create your tests here.
