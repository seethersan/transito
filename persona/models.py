from django.db import models


class Persona(models.Model):
    email = models.EmailField(max_length=50, primary_key=True)
    first_name = models.CharField(max_length=50, null=False, blank=False)
    last_name = models.CharField(max_length=50, null=False, blank=False)
