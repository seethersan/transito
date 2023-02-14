from django.test import TestCase
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APIClient
from vehiculo.models import Vehiculo, Infraccion
from persona.models import Persona
from policia.models import Policia


class VehiculoViewSetTestCase(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.persona = Persona.objects.create(
            email="test@example.com", first_name="John", last_name="Doe"
        )
        self.vehiculo_data = {
            "placa": "ABC123",
            "marca": "Chevrolet",
            "modelo": "Sonic",
            "color": "Azul",
            "tipo": "Automóvil",
            "propietario": self.persona,
        }
        self.vehiculo = Vehiculo.objects.create(**self.vehiculo_data)

    def test_list_vehicles_empty(self):
        url = "/api/infracciones/?email=test@example.com"
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data, [])

    def test_create_vehicle(self):
        user = Policia.objects.create_user(
            username="testuser", password="testpass"
        )
        self.client.force_authenticate(user=user)
        new_vehiculo_data = {
            "placa": "XYZ123",
            "marca": "Nissan",
            "modelo": "Sentra",
            "color": "Negro",
            "tipo": "Automóvil",
            "propietario": "test@example.com",
        }
        url = "/api/vehiculos/"
        response = self.client.post(url, new_vehiculo_data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Vehiculo.objects.count(), 2)

    def test_create_infraccion(self):
        user = Policia.objects.create_user(
            username="testuser", password="testpass"
        )
        self.client.force_authenticate(user=user)
        infraccion_data = {
            "placa_patente": self.vehiculo_data["placa"],
            "lugar": "Av. Siempre Viva",
            "timestamp": "2023-02-14T10:00:00Z",
            "comentarios": "Estacionamiento en lugar prohibido",
        }
        url = "/api/infracciones/?email=test@example.com"
        response = self.client.post(url, infraccion_data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Infraccion.objects.count(), 1)

    def test_create_infraccion_unauthenticated(self):
        infraccion_data = {
            "placa_patente": self.vehiculo_data["placa"],
            "lugar": "Av. Siempre Viva",
            "timestamp": "2023-02-14T10:00:00Z",
            "comentarios": "Estacionamiento en lugar prohibido",
        }
        url = "/api/infracciones/?email=test@example.com"
        response = self.client.post(url, infraccion_data)
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)
        self.assertEqual(Infraccion.objects.count(), 0)