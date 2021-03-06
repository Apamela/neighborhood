from django.test import TestCase
from .models import Profile,Business,Post,Neighborhood,EmergencyContacts
# Create your tests here.
class UserProfileTestClass(TestCase):
    def setUp(self):
        self.new_user = User.objects.create_user(username='user',password='user-password')
        self.new_profile = Profile(id=1,first_name='Firstname',last_name='Lastname',user=self.new_user,location='Test Location')
        self.new_neighborhood = Neighborhood(id=1,neighborhood_name='Test Neighborhood')

    def test_instance(self):
        self.assertTrue(isinstance(self.new_profile,Profile))

    def test_save_profile(self):
        self.new_profile.save_profile()
        profiles = Profile.objects.all()
        self.assertTrue(len(profiles) > 0)

    def test_delete_profile(self):
        self.new_profile.delete_profile()
        profiles = Profile.objects.all()
        self.assertTrue(len(profiles) == 0)

    def test_assign_neighborhood(self):

        self.new_profile.save_profile()
        profile = Profile.objects.filter(id=1).first()
        self.new_neighborhood.save()
        neighborhood = Neighborhood.objects.filter(id=1).first()
        profile.assign_neighborhood(neighborhood)

        self.assertEqual(profile.neighborhood.id,1)

class NeighborhoodTestClass(TestCase):
    def setUp(self):
        self.new_neighborhood = Neighborhood(id=1,neighborhood_name='Test Neighborhood')

    def test_instance(self):
        self.assertTrue(isinstance(self.new_neighborhood,Neighborhood))

    def test_create_neighborhood(self):
        self.new_neighborhood.create_neighborhood()
        neighborhoods = Neighborhood.objects.all()
        self.assertTrue(len(neighborhoods) > 0)

    def test_delete_neighborhood(self):
        self.new_neighborhood.delete_neighborhood()
        neighborhoods = Neighborhood.objects.all()
        self.assertTrue(len(neighborhoods) == 0)

    def test_find_neighborhood(self):
        self.new_neighborhood.create_neighborhood()
        neighborhood = Neighborhood.find_neighborhood(1)
        self.assertEqual(neighborhood.neighborhood_name,'Test Neighborhood')

    def test_update_neighborhood(self):
        self.new_neighborhood.create_neighborhood()
        neighborhood = Neighborhood.find_neighborhood(1)
        neighborhood.neighborhood_name = 'Another Neighborhood'
        self.assertEqual(neighborhood.neighborhood_name,'Another Neighborhood')


class BusinessTestClass(TestCase):
    def setUp(self):
        self.new_user = User.objects.create_user(username='user',password='user-password')
        self.new_neighborhood = Neighborhood(id=1,neighborhood_name='Test Neighborhood')
        self.new_neighborhood.save()
        self.new_business = Business(id = 1,name='Test Business',owner=self.new_user,business_location='Test Location',business_neighborhood=self.new_neighborhood,email='business@email.com')

    def test_instance(self):
        self.assertTrue(isinstance(self.new_business,Business))

    def test_create_business(self):
        self.new_business.create_business()
        businesses = Business.objects.all()
        self.assertTrue(len(businesses) > 0)

    def test_delete_business(self):
        self.new_business.delete_business()
        businesses = Business.objects.all()
        self.assertTrue(len(businesses) == 0)

    def test_find_business(self):
        self.new_business.create_business()
        business = Business.find_business(1)
        self.assertEqual(business.name,'Test Business')

    def test_update_business(self):
        self.new_business.create_business()
        business = Business.find_business(1)
        business.update_business('Another Business')
        self.assertEqual(business.name,'Another Business')


