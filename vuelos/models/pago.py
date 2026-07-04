from django.db import models
from .reserva     import Reserva
from .metodo_pago import MetodoPago

class Pago(models.Model):

    class Estado(models.TextChoices):
        PENDIENTE  = 'pendiente',  'Pendiente'
        COMPLETADO = 'completado', 'Completado'
        FALLIDO    = 'fallido',    'Fallido'
        REEMBOLSADO = 'reembolsado', 'Reembolsado'

    reserva      = models.ForeignKey(Reserva,    on_delete=models.PROTECT, related_name='pagos')
    metodo_pago  = models.ForeignKey(MetodoPago, on_delete=models.PROTECT, related_name='pagos')
    monto        = models.DecimalField(max_digits=10, decimal_places=2)
    estado       = models.CharField(max_length=20, choices=Estado.choices, default=Estado.PENDIENTE)
    referencia   = models.CharField(max_length=100, blank=True)
    fecha        = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name        = 'Pago'
        verbose_name_plural = 'Pagos'
        ordering            = ['-fecha']

    def __str__(self):
        return f'Pago #{self.pk} — {self.monto} — {self.estado}'
