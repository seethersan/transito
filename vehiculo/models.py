from django.db import models


from persona.models import Persona

class Vehiculo(models.Model):
    placa = models.CharField(max_length=10, null=False, blank=False, unique=True)
    marca = models.CharField(max_length=20, null=False, blank=False)
    modelo = models.CharField(max_length=20, null=False, blank=False)
    color = models.CharField(max_length=20, null=False, blank=False)
    tipo = models.CharField(max_length=20, null=False, blank=False)
    propietario = models.ForeignKey(Persona, on_delete=models.CASCADE)

    def __str__(self):
        return self.placa