from django.db import models
from django.contrib.auth.models import User


class Pasajero(models.Model):
    usuario           = models.OneToOneField(User, on_delete=models.CASCADE, related_name='pasajero')
    numero_pasaporte  = models.CharField(max_length=20, unique=True)
    nacionalidad      = models.CharField(max_length=100)
    fecha_nacimiento  = models.DateField()
    telefono          = models.CharField(max_length=20, blank=True)

    class Meta:
        verbose_name        = 'Pasajero'
        verbose_name_plural = 'Pasajeros'
        ordering            = ['usuario__last_name']

    def __str__(self):
        return f'{self.usuario.get_full_name()} ({self.numero_pasaporte})'