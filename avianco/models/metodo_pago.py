from django.db import models

class MetodoPago(models.Model):

    class Tipo(models.TextChoices):
        TARJETA   = 'tarjeta',   'Tarjeta de Crédito/Débito'
        PAYPAL    = 'paypal',    'PayPal'
        TRANSFER  = 'transferencia', 'Transferencia Bancaria'
        EFECTIVO  = 'efectivo',  'Efectivo'

    nombre = models.CharField(max_length=100)
    tipo   = models.CharField(max_length=20, choices=Tipo.choices)
    activo = models.BooleanField(default=True)

    class Meta:
        verbose_name        = 'Método de Pago'
        verbose_name_plural = 'Métodos de Pago'
        ordering            = ['tipo', 'nombre']

    def __str__(self):
        return f'{self.nombre} ({self.get_tipo_display()})'
