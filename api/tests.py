import names
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase


class TestApi(APITestCase):

    mothership = None

    def setUp(self):
        response = self.client.post(reverse('mothership_list'))
        self.mothership = self.client.get(
            reverse('mothership_details', kwargs={'pk': response.data['id']})).data

    def test_create_mothership(self):
        response = self.client.post(reverse('mothership_list'))
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_default_ship_creation(self):
        self.assertEqual(len(self.mothership['ships']), 3)

    def test_create_ship(self):
        response = self.client.post(reverse('ship_list'), {'mothership': self.mothership['id']})
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_create_ship_with_count(self):
        response = self.client.post(reverse('ship_list'), {'mothership': self.mothership['id'], 'count': 2})
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(len(response.data), 2)

    def test_create_crew(self):
        ship = self.mothership['ships'][0]
        response = self.client.post(reverse('crew_list'), {'name': names.get_first_name(), 'ship': ship['id']})
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_default_create_crew(self):
        ship = self.mothership['ships'][0]
        response = self.client.get(reverse('ship_details', kwargs={'pk': ship['id']}))
        self.assertEqual(len(response.data['crew']), 3)

    def test_ship_vacancy(self):
        ship = self.mothership['ships'][0]
        for i in range(3):
            response = self.client.post(reverse('crew_list'), {'name': names.get_first_name(), 'ship': ship['id']})
        self.assertEqual(response.status_code, status.HTTP_405_METHOD_NOT_ALLOWED)
        ship = self.client.get(reverse('ship_details', kwargs={'pk': ship['id']})).data
        self.assertEqual(len(ship['crew']), 5)

    def test_swap_crew(self):
        from_ship = self.mothership['ships'][0]
        to_ship = self.mothership['ships'][1]
        crew = self.client.post(reverse('crew_list'), {'name': names.get_first_name(), 'ship': from_ship['id']}).data
        response = self.client.put(reverse('crew_list'), {'from_ship': from_ship['id'], 'to_ship': to_ship['id'], 'name': crew['name']})
        self.assertEqual(response.data['ship'], to_ship['id'])

