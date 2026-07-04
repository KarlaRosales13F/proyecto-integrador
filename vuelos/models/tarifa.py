from django.db import models

class Tarifa(models.Model):

    class Clase(models.TextChoices):
        ECONOMICA = 'economica', 'Económica'
        BUSINESS  = 'business',  'Business'
        PRIMERA   = 'primera',   'Primera Clase'

    nombre      = models.CharField(max_length=100)
    clase       = models.CharField(max_length=20, choices=Clase.choices, default=Clase.ECONOMICA)
    descripcion = models.TextField(blank=True)
    descuento   = models.DecimalField(max_digits=5, decimal_places=2, default=0)

    class Meta:
        verbose_name        = 'Tarifa'
        verbose_name_plural = 'Tarifas'
        ordering            = ['clase', 'nombre']

    def __str__(self):
        return f'{self.nombre} ({self.get_clase_display()})'
