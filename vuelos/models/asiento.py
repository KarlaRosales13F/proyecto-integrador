from django.db import models
from .vuelo import Vuelo


class Asiento(models.Model):

    class Clase(models.TextChoices):
        ECONOMICA = 'economica', 'Económica'
        BUSINESS  = 'business',  'Business'
        PRIMERA   = 'primera',   'Primera Clase'

    vuelo      = models.ForeignKey(Vuelo, on_delete=models.CASCADE, related_name='asientos')
    codigo     = models.CharField(max_length=5)
    clase      = models.CharField(max_length=20, choices=Clase.choices, default=Clase.ECONOMICA)
    fila       = models.PositiveIntegerField()
    columna    = models.CharField(max_length=2)
    disponible = models.BooleanField(default=True)

    class Meta:
        verbose_name        = 'Asiento'
        verbose_name_plural = 'Asientos'
        ordering            = ['vuelo', 'fila', 'columna']
        unique_together     = [['vuelo', 'codigo']]

    def __str__(self):
        return f'Asiento {self.codigo} ({self.get_clase_display()}) — {self.vuelo}'
