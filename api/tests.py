from django.urls import reverse
from rest_framework.test import APITestCase

class TestApi(APITestCase):


    def test_create_mothership(self):
        response = self.client.post(reverse('mothership_list'))
        print(response.data)
        self.assertEqual(response.status_code, 201)

    def test_crew_swap(self):
        assert True

    # Test Create
    # test ship create with count
    # test
    # Test crew swap