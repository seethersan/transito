from django.db import models


from persona.models import Persona
from policia.models import Policia


class Vehiculo(models.Model):
    placa = models.CharField(max_length=10, primary_key=True)
    marca = models.CharField(max_length=20, null=False, blank=False)
    modelo = models.CharField(max_length=20, null=False, blank=False)
    color = models.CharField(max_length=20, null=False, blank=False)
    tipo = models.CharField(max_length=20, null=False, blank=False)
    propietario = models.ForeignKey(Persona, on_delete=models.CASCADE)

    def __str__(self):
        return self.placa


class Infraccion(models.Model):
    vehiculo = models.ForeignKey(Vehiculo, on_delete=models.CASCADE)
    timestamp = models.DateTimeField(null=False, blank=False)
    lugar = models.CharField(max_length=50, null=False, blank=False)
    comentarios = models.CharField(max_length=200, null=False, blank=False)
    policia = models.ForeignKey(Policia, on_delete=models.CASCADE)

    class Meta:
        unique_together = ("vehiculo", "timestamp", "lugar", "comentarios")

    def __str__(self):
        return self.vehiculo.placa
