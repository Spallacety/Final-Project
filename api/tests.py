from django.test import *
from rest_framework.reverse import reverse
from rest_framework import status
import json

class APITest(TestCase):
  fixtures = ['fixtures.json']

  def auth(self):
    self.client.post("/auth/login/", {"username": "lucas", "password": "xpto"})

  def test_employee_list_unauth(self):
    response = self.client.get(reverse('employee-list'))
    self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)

  def test_employee_list_auth(self):
    self.auth()
    response = self.client.get(reverse('employee-list'))
    self.assertEqual(response.status_code, status.HTTP_200_OK)

  def test_employee_detail_unauth(self):
    response = self.client.get(reverse('employee-detail', args=[1]))
    self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)

  def test_employee_detail_auth(self):
    self.auth()
    response = self.client.get(reverse('employee-detail', args=[1]))
    self.assertEqual(response.status_code, status.HTTP_200_OK)

  def test_client_list(self):
    response = self.client.get(reverse('client-list'))
    self.assertEqual(response.status_code, status.HTTP_200_OK)

  def test_client_detail(self):
    response = self.client.get(reverse('client-detail', args=[1]))
    self.assertEqual(response.status_code, status.HTTP_200_OK)

  def test_new_client_unauth(self):
    request_data = {"name": "New Client",
                    "address": "157 Test Street, Nice City, NS",
                    "phone": "0 1234 5678"}
    response = self.client.post(reverse('client-list'), json.dumps(request_data), 'application/json')
    self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)

  def test_new_client_auth(self):
    self.auth()
    request_data = {"name": "New Client",
                    "address": "157 Test Street, Nice City, NS",
                    "phone": "0 1234 5678"}
    response = self.client.post(reverse('client-list'), json.dumps(request_data), 'application/json')
    self.assertEqual(response.status_code, status.HTTP_201_CREATED)

  def test_update_client_unauth(self):
    request_data = {"id": 100,
                    "name": "New Client",
                    "address": "157 Test Street, Nice City, NS",
                    "phone": "0 1234 5678"}
    response = self.client.put(reverse('client-detail', args=[1]), json.dumps(request_data), 'application/json')
    self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)

  def test_update_client_auth(self):
    self.auth()
    request_data = {"id": 100,
                    "name": "New Client",
                    "address": "157 Test Street, Nice City, NS",
                    "phone": "0 1234 5678"}
    response = self.client.put(reverse('client-detail', args=[1]), json.dumps(request_data), 'application/json')
    self.assertEqual(response.status_code, status.HTTP_200_OK)

  def test_delete_client_unauth(self):
    response = self.client.delete(reverse('client-detail', args=[1]))
    self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)

  def test_delete_client_auth(self):
    self.auth()
    response = self.client.delete(reverse('client-detail', args=[1]))
    self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)

  def test_product_list(self):
    response = self.client.get(reverse('product-list'))
    self.assertEqual(response.status_code, status.HTTP_200_OK)

  def test_product_detail(self):
    response = self.client.get(reverse('product-detail', args=[1]))
    self.assertEqual(response.status_code, status.HTTP_200_OK)

  def test_new_product_unauth(self):
    request_data = {"description": "New Product",
                    "price": 5.0}
    response = self.client.post(reverse('product-list'), json.dumps(request_data), 'application/json')
    self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)

  def test_new_product_auth(self):
    self.auth()
    request_data = {"description": "New Product",
                    "price": 5.0}
    response = self.client.post(reverse('product-list'), json.dumps(request_data), 'application/json')
    self.assertEqual(response.status_code, status.HTTP_201_CREATED)

  def test_update_product_unauth(self):
    request_data = {"id": 100,
                    "description": "New Product",
                    "price": 5.0}
    response = self.client.put(reverse('product-detail', args=[1]), json.dumps(request_data), 'application/json')
    self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)

  def test_update_product_auth(self):
    self.auth()
    request_data = {"id": 100,
                    "description": "New Product",
                    "price": 5.0}
    response = self.client.put(reverse('product-detail', args=[1]), json.dumps(request_data), 'application/json')
    self.assertEqual(response.status_code, status.HTTP_200_OK)

  def test_delete_product_unauth(self):
    response = self.client.delete(reverse('product-detail', args=[1]))
    self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)

  def test_delete_product_auth(self):
    self.auth()
    response = self.client.delete(reverse('product-detail', args=[1]))
    self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)

  def test_sale_list(self):
    response = self.client.get(reverse('sale-list'))
    self.assertEqual(response.status_code, status.HTTP_200_OK)

  def test_sale_detail(self):
    response = self.client.get(reverse('sale-detail', args=[1]))
    self.assertEqual(response.status_code, status.HTTP_200_OK)

  def test_new_sale_unauth(self):
    request_data = {"client": "Ronaldo Santos"}
    response = self.client.post(reverse('sale-list'), json.dumps(request_data), 'application/json')
    self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)

  def test_new_sale_auth(self):
    self.auth()
    request_data = {"client": "Ronaldo Santos"}
    response = self.client.post(reverse('sale-list'), json.dumps(request_data), 'application/json')
    self.assertEqual(response.status_code, status.HTTP_201_CREATED)

  def test_delete_sale_unauth(self):
    response = self.client.delete(reverse('sale-detail', args=[1]))
    self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)

  def test_delete_my_sale_auth(self):
    self.auth()
    response = self.client.delete(reverse('sale-detail', args=[2]))
    self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)

  def test_delete_other_sale_auth(self):
    self.auth()
    response = self.client.delete(reverse('sale-detail', args=[1]))
    self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)

  def test_sale_item_list(self):
    response = self.client.get(reverse('saleitem-list'))
    self.assertEqual(response.status_code, status.HTTP_200_OK)

  def test_sale_item_detail(self):
    response = self.client.get(reverse('saleitem-detail', args=[1]))
    self.assertEqual(response.status_code, status.HTTP_200_OK)

  def test_new_item_on_sale_unauth(self):
    request_data = {"sale": reverse('sale-detail', args=[1]),
                    "product": "Leite",
                    "quantity": 2,}
    response = self.client.post(reverse('saleitem-list'), json.dumps(request_data), 'application/json')
    self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)

  def test_new_item_on_my_sale_auth(self):
    self.auth()
    request_data = {"sale": reverse('sale-detail', args=[2]),
                    "product": "Leite",
                    "quantity": 2, }
    response = self.client.post(reverse('saleitem-list'), json.dumps(request_data), 'application/json')
    self.assertEqual(response.status_code, status.HTTP_201_CREATED)

  def test_new_item_on_other_sale_auth(self):
    self.auth()
    request_data = {"sale": reverse('sale-detail', args=[1]),
                    "product": "Leite",
                    "quantity": 2, }
    response = self.client.post(reverse('saleitem-list'), json.dumps(request_data), 'application/json')
    self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)

  def test_delete_item_on_sale_unauth(self):
    response = self.client.delete(reverse('saleitem-detail', args=[1]))
    self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)

  def test_delete_item_on_my_sale_auth(self):
    self.auth()
    response = self.client.delete(reverse('saleitem-detail', args=[4]))
    self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)

  def test_delete_item_on_other_sale_auth(self):
    self.auth()
    response = self.client.delete(reverse('saleitem-detail', args=[1]))
    self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)
