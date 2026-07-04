from django.db import models
from .reserva import Reserva


class CheckIn(models.Model):

    class Estado(models.TextChoices):
        CHECKIN  = 'checkin',  'Check-in'
        EMBARCADO = 'embarcado', 'Embarcado'

    reserva          = models.OneToOneField(Reserva, on_delete=models.CASCADE, related_name='checkin')
    hora_checkin     = models.DateTimeField(auto_now_add=True)
    puerta           = models.CharField(max_length=10, blank=True)
    tarjeta_embarque = models.TextField(blank=True)
    estado           = models.CharField(max_length=20, choices=Estado.choices, default=Estado.CHECKIN)

    class Meta:
        verbose_name        = 'Check-in'
        verbose_name_plural = 'Check-ins'
        ordering            = ['-hora_checkin']

    def __str__(self):
        return f'CheckIn — Reserva #{self.reserva.pk} — {self.estado}'
