from django.db import models
from .reserva import Reserva

class CheckIn(models.Model):

    class Metodo(models.TextChoices):
        WEB      = 'web',      'Web'
        APP      = 'app',      'App Móvil'
        MOSTRADOR = 'mostrador', 'Mostrador'

    reserva        = models.OneToOneField(Reserva, on_delete=models.CASCADE, related_name='checkin')
    fecha_checkin  = models.DateTimeField(auto_now_add=True)
    metodo         = models.CharField(max_length=15, choices=Metodo.choices, default=Metodo.WEB)
    asiento_final  = models.CharField(max_length=5)
    equipaje_listo = models.BooleanField(default=False)
    pase_abordar   = models.CharField(max_length=50, blank=True, help_text='Código del pase de abordar')

    class Meta:
        verbose_name        = 'Check-In'
        verbose_name_plural = 'Check-Ins'
        ordering            = ['-fecha_checkin']

    def __str__(self):
        return f'CheckIn — Reserva #{self.reserva_id} | Asiento {self.asiento_final}'
