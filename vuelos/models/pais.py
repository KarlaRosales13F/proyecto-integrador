from django.db import models

class Pais(models.Model):
    nombre     = models.CharField(max_length=100, unique=True)
    codigo     = models.CharField(max_length=3, unique=True)
    bandera    = models.URLField(blank=True)

    class Meta:
        verbose_name        = 'País'
        verbose_name_plural = 'Países'
        ordering            = ['nombre']

    def __str__(self):
        return self.nombre
