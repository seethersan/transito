from django.db import models
from django.contrib.auth.models import AbstractUser


class Policia(AbstractUser):
    nui = models.CharField(max_length=10, null=False, blank=False, unique=True)
