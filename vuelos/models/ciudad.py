from django.db import models
from .pais import Pais

class Ciudad(models.Model):
    nombre = models.CharField(max_length=100)
    pais   = models.ForeignKey(Pais, on_delete=models.PROTECT, related_name='ciudades')

    class Meta:
        verbose_name        = 'Ciudad'
        verbose_name_plural = 'Ciudades'
        ordering            = ['nombre']
        unique_together     = [['nombre', 'pais']]

    def __str__(self):
        return f'{self.nombre}, {self.pais.nombre}'
