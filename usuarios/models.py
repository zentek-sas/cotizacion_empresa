from django.contrib.auth.models import AbstractUser
from django.db import models

class UsuarioCustom(AbstractUser):
    telefono = models.CharField(max_length=20, blank=True)
    empresa = models.CharField(max_length=100, blank=True)
    puesto = models.CharField(max_length=100, blank=True)

    class Meta:
        verbose_name = 'Usuario'
        verbose_name_plural = 'Usuarios'

    def __str__(self):
        return self.email
# Create your models here.
