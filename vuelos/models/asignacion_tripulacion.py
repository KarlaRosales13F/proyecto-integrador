from django.db import models
from .vuelo      import Vuelo
from .tripulacion import Tripulacion

class AsignacionTripulacion(models.Model):
    vuelo       = models.ForeignKey(Vuelo,      on_delete=models.PROTECT, related_name='tripulacion')
    tripulacion = models.ForeignKey(Tripulacion, on_delete=models.PROTECT, related_name='asignaciones')
    fecha_asignacion = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name        = 'Asignación de Tripulación'
        verbose_name_plural = 'Asignaciones de Tripulación'
        unique_together     = [['vuelo', 'tripulacion']]

    def __str__(self):
        return f'{self.tripulacion} en {self.vuelo}'
