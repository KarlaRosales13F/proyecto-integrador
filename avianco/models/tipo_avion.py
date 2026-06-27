from django.db import models

class TipoAvion(models.Model):
    nombre       = models.CharField(max_length=100, unique=True)
    fabricante   = models.CharField(max_length=100)
    autonomia_km = models.PositiveIntegerField()
    descripcion  = models.TextField(blank=True)

    class Meta:
        verbose_name        = 'Tipo de Avión'
        verbose_name_plural = 'Tipos de Avión'
        ordering            = ['fabricante', 'nombre']

    def __str__(self):
        return f'{self.fabricante} {self.nombre}'
