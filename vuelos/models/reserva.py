from django.db import models
from .vuelo    import Vuelo
from .pasajero import Pasajero


class Reserva(models.Model):

    class Estado(models.TextChoices):
        CONFIRMADA  = 'confirmada',  'Confirmada'
        CANCELADA   = 'cancelada',   'Cancelada'
        EMBARCADO   = 'embarcado',   'Embarcado'

    vuelo      = models.ForeignKey(Vuelo,    on_delete=models.PROTECT, related_name='reservas')
    pasajero   = models.ForeignKey(Pasajero, on_delete=models.PROTECT, related_name='reservas')
    asiento    = models.CharField(max_length=5)
    estado     = models.CharField(max_length=20, choices=Estado.choices, default=Estado.CONFIRMADA)
    fecha_reserva = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name        = 'Reserva'
        verbose_name_plural = 'Reservas'
        ordering            = ['-fecha_reserva']
        unique_together     = [['vuelo', 'asiento']]

    def __str__(self):
        return f'Reserva #{self.pk} — {self.pasajero} en {self.vuelo}'