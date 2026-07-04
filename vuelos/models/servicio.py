from django.db import models
from .reserva import Reserva


class Servicio(models.Model):

    class Tipo(models.TextChoices):
        COMIDA    = 'comida',    'Comida'
        EQUIPAJE  = 'equipaje',  'Equipaje Extra'
        ASIENTO   = 'asiento',   'Selección de Asiento'
        WIFI      = 'wifi',      'WiFi'
        SEGURO    = 'seguro',    'Seguro de Viaje'
        OTRO      = 'otro',      'Otro'

    nombre      = models.CharField(max_length=100)
    descripcion = models.TextField(blank=True)
    precio      = models.DecimalField(max_digits=8, decimal_places=2)
    tipo        = models.CharField(max_length=20, choices=Tipo.choices, default=Tipo.OTRO)

    class Meta:
        verbose_name        = 'Servicio'
        verbose_name_plural = 'Servicios'
        ordering            = ['tipo', 'nombre']

    def __str__(self):
        return f'{self.nombre} ({self.get_tipo_display()})'


class ReservaServicio(models.Model):
    reserva        = models.ForeignKey(Reserva, on_delete=models.CASCADE, related_name='servicios')
    servicio       = models.ForeignKey(Servicio, on_delete=models.CASCADE, related_name='reservas')
    cantidad       = models.PositiveIntegerField(default=1)
    precio_aplicado = models.DecimalField(max_digits=8, decimal_places=2)

    class Meta:
        verbose_name        = 'Reserva Servicio'
        verbose_name_plural = 'Reserva Servicios'
        unique_together     = [['reserva', 'servicio']]

    def __str__(self):
        return f'{self.servicio.nombre} x{self.cantidad} — Reserva #{self.reserva.pk}'
