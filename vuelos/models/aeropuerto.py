from django.db import models


class Aeropuerto(models.Model):
    codigo_iata = models.CharField(max_length=3, unique=True)
    nombre      = models.CharField(max_length=150)
    ciudad      = models.CharField(max_length=100)
    pais        = models.CharField(max_length=100)

    class Meta:
        verbose_name        = 'Aeropuerto'
        verbose_name_plural = 'Aeropuertos'
        ordering            = ['pais', 'ciudad']

    def __str__(self):
        return f'{self.codigo_iata} — {self.nombre}'