from django.db import models
from .aeropuerto import Aeropuerto

class Terminal(models.Model):
    aeropuerto = models.ForeignKey(Aeropuerto, on_delete=models.PROTECT, related_name='terminales')
    nombre     = models.CharField(max_length=50)
    descripcion = models.TextField(blank=True)

    class Meta:
        verbose_name        = 'Terminal'
        verbose_name_plural = 'Terminales'
        ordering            = ['aeropuerto', 'nombre']

    def __str__(self):
        return f'Terminal {self.nombre} — {self.aeropuerto.codigo_iata}'
