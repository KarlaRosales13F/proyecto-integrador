from django.db import models


class Aerolinea(models.Model):
    nombre    = models.CharField(max_length=150)
    codigo    = models.CharField(max_length=10, unique=True)
    pais      = models.CharField(max_length=100)
    sitio_web = models.URLField(blank=True)

    class Meta:
        verbose_name        = 'Aerolínea'
        verbose_name_plural = 'Aerolíneas'
        ordering            = ['nombre']

    def __str__(self):
        return f'{self.codigo} — {self.nombre}'
