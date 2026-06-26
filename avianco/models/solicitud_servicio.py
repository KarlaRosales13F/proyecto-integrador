from django.db import models
from .reserva import Reserva

class SolicitudServicio(models.Model):

    class TipoServicio(models.TextChoices):
        COMIDA_ESPECIAL  = 'comida_especial',  'Comida Especial'
        SILLA_RUEDAS     = 'silla_ruedas',     'Silla de Ruedas'
        ASISTENCIA_MENOR = 'asistencia_menor', 'Asistencia a Menor'
        MASCOTAS         = 'mascotas',          'Transporte de Mascotas'
        OTRO             = 'otro',              'Otro'

    class Estado(models.TextChoices):
        PENDIENTE = 'pendiente', 'Pendiente'
        APROBADO  = 'aprobado',  'Aprobado'
        RECHAZADO = 'rechazado', 'Rechazado'

    reserva         = models.ForeignKey(Reserva, on_delete=models.CASCADE, related_name='solicitudes_servicio')
    tipo_servicio   = models.CharField(max_length=30, choices=TipoServicio.choices)
    descripcion     = models.TextField(blank=True)
    estado          = models.CharField(max_length=15, choices=Estado.choices, default=Estado.PENDIENTE)
    fecha_solicitud = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name        = 'Solicitud de Servicio'
        verbose_name_plural = 'Solicitudes de Servicio'
        ordering            = ['-fecha_solicitud']

    def __str__(self):
        return f'{self.get_tipo_servicio_display()} — Reserva #{self.reserva_id} ({self.estado})'
