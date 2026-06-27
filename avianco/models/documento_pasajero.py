from django.db import models
from .pasajero import Pasajero

class DocumentoPasajero(models.Model):

    class TipoDocumento(models.TextChoices):
        PASAPORTE = 'pasaporte', 'Pasaporte'
        VISA      = 'visa',      'Visa'
        DNI       = 'dni',       'DNI / Cédula'
        OTRO      = 'otro',      'Otro'

    pasajero          = models.ForeignKey(Pasajero, on_delete=models.CASCADE, related_name='documentos')
    tipo              = models.CharField(max_length=15, choices=TipoDocumento.choices)
    numero            = models.CharField(max_length=50)
    pais_emisor       = models.CharField(max_length=100)
    fecha_emision     = models.DateField()
    fecha_vencimiento = models.DateField()
    activo            = models.BooleanField(default=True)

    class Meta:
        verbose_name        = 'Documento de Pasajero'
        verbose_name_plural = 'Documentos de Pasajeros'
        ordering            = ['pasajero', 'tipo']
        unique_together     = [['pasajero', 'tipo', 'numero']]

    def __str__(self):
        return f'{self.get_tipo_display()} {self.numero} — {self.pasajero}'
