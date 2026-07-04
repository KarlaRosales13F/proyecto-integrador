from django.db import models
from .reserva import Reserva


class Factura(models.Model):

    class Estado(models.TextChoices):
        PENDIENTE = 'pendiente', 'Pendiente'
        PAGADA    = 'pagada',    'Pagada'
        ANULADA   = 'anulada',   'Anulada'

    reserva   = models.ForeignKey(Reserva, on_delete=models.PROTECT, related_name='facturas')
    total     = models.DecimalField(max_digits=10, decimal_places=2)
    impuestos = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    estado    = models.CharField(max_length=20, choices=Estado.choices, default=Estado.PENDIENTE)
    fecha     = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name        = 'Factura'
        verbose_name_plural = 'Facturas'
        ordering            = ['-fecha']

    def __str__(self):
        return f'Factura #{self.pk} — Reserva #{self.reserva.pk} — {self.estado}'
