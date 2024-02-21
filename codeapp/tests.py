from django.urls import reverse
from rest_framework import status
from rest_framework.test import APIClient, APITestCase
from .models import Career

class ProdutoAPITestCase(APITestCase):
    def setUp(self):
        self.client = APIClient()
        self.career_data = {
            'username': 'Career Name',
            'title': 'Career Title',
            'content': 'Career Content'
        }
        self.career = Career.objects.create(**self.career_data)

    def test_list_carrers(self):
        url = reverse('codeapp:career_list')
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_create_career(self):
        url = reverse('codeapp:career_list')
        response = self.client.post(url, self.career_data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_create_career_with_invalid_payload(self):
        url = reverse('codeapp:career_list')
        response = self.client.post(url, {}, format='json')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_retrieve_career(self):
        url = reverse('codeapp:career_detail', args=[self.career.id])
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['username'], self.career_data['username'])

    def test_retrieve_career_with_invalid_id(self):
        url = reverse('codeapp:career_detail', args=[999])
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)
        self.assertEqual(response.data['error'], "Career not found.")

    def test_update_career(self):
        updated_data = {
            'username': 'Career Updated',
        }
        url = reverse('codeapp:career_detail', args=[self.career.id])
        response = self.client.put(url, updated_data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['username'], updated_data['username'])

    def test_delete_career(self):
        url = reverse('codeapp:career_detail', args=[self.career.id])
        response = self.client.delete(url)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
