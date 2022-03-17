from django.test import TestCase
from django.contrib.auth import get_user_model

from .models import Travel

class TravelTests(TestCase):

    @classmethod
    def setUpTestData(cls):
        testuser1 = get_user_model().objects.create_user(username='testuser', password='pass')
        testuser1.save()

        test_travel = Travel.objects.create(name='rake', owner=testuser1,description='Better for collecting leaves than a shovel.')
        test_travel.save()

    def test_things_model(self):
        travel = Travel.objects.get(id=1)
        actual_owner = str(travel.owner)
        actual_name = str(travel.name)
        actual_description = str(travel.description)
        self.assertEqual(actual_owner,'testuser')
        self.assertEqual(actual_name, 'rake')
        self.assertEqual(actual_description,'Better for collecting leaves than a shovel.')