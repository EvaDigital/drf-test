from django.test import TestCase
from rest_framework.test import APIClient
from rest_framework import status
from .models import Advert, City, Category


class AdvertListTestCase(TestCase):
    def setUp(self):
        self.client = APIClient()

        # Create multiple Advert for testing
        self.city1 = City.objects.create(name='City 1')
        self.city2 = City.objects.create(name='City 2')

        self.category1 = Category.objects.create(name='Category 1')
        self.category2 = Category.objects.create(name='Category 2')

        self.advert1 = Advert.objects.create(
            title='Advert 1',
            description='Description 1',
            city=self.city1,
            category=self.category1
        )

        self.advert2 = Advert.objects.create(
            title='Advert 2',
            description='Description 2',
            city=self.city2,
            category=self.category2
        )


    def test_get_advert_list(self):
        """
            Verifies that a GET /api/advert-list/ request returns a list of adverts
        """
        response = self.client.get('/api/advert-list/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 2)  # Checking the adverts count


class AdvertDetailTestCase(TestCase):
    def setUp(self):
        self.client = APIClient()
        # Create multiple Advert for testing
        self.city = City.objects.create(name='City 1')
        self.category = Category.objects.create(name='Category 1')
        self.advert = Advert.objects.create(
            title='Advert 1',
            description='Description 1',
            city=self.city,
            category=self.category
        )

    def test_get_advert_detail(self):
        """
            Checks that a GET /api/advert/<id>/ request returns the details of the adverts
        """
        response = self.client.get(f'/api/advert/{self.advert.id}/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['id'], self.advert.id)  # Checking the advert ID

    def test_increment_view_count(self):
        """
            Checks that viewing the ad details increases the view count
        """
        initial_views = self.advert.views
        response = self.client.get(f'/api/advert/{self.advert.id}/')
        updated_advert = Advert.objects.get(pk=self.advert.id)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(updated_advert.views, initial_views + 1)  # Checking the increase of the view counter
