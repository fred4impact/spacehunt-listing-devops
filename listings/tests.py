# from django.test import TestCase
# from users.models import User
# from .models import Property, Location
# # Create your tests here.


# class PropertyModelTest(TestCase):
#     @classmethod
#     def setUpTestData(cls):
#         # Create a test user
#         user = User.objects.create_user( email='test@example.com', password='password')

#         # Create a test location
#         location = Location.objects.create(country='Test Location', street='street', city='city', state='state', postal_code='test')

#         # Create a test property
#         property = Property.objects.create(
#             name='Test Property',
#             description='Test description',
#             property_type='deluxe_houses',
#             location=location,
#             price=100000.00,
#             bedrooms=3,
#             bathrooms=2.5,
#             garage=2,
#             total_area=150.0,
#             status='sale',
#             realtor=user
#         )

#     def test_property_is_visible(self):
#         property = Property.objects.get(pk=pk)  # Get the Property instance from the database
#         self.assertEqual(property.is_visible(), False)  # Expected publish value is 'draft'

#     def test_property_str_method(self):
#         property = Property.objects.get(pk=pk)  # Get the Property instance from the database
#         expected_str = property.name
#         self.assertEqual(str(property), expected_str)





