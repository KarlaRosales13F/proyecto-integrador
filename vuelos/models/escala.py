from django.db import models
from .vuelo      import Vuelo
from .aeropuerto import Aeropuerto

class Escala(models.Model):
    vuelo           = models.ForeignKey(Vuelo,      on_delete=models.CASCADE,  related_name='escalas')
    aeropuerto      = models.ForeignKey(Aeropuerto, on_delete=models.PROTECT,  related_name='escalas')
    orden           = models.PositiveIntegerField()
    llegada         = models.DateTimeField()
    salida          = models.DateTimeField()

    class Meta:
        verbose_name        = 'Escala'
        verbose_name_plural = 'Escalas'
        ordering            = ['vuelo', 'orden']
        unique_together     = [['vuelo', 'orden']]

    def __str__(self):
        return f'Escala {self.orden} — {self.aeropuerto.codigo_iata} en {self.vuelo}'
