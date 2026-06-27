from django.db import models
from .aeronave import Aeronave

class MantenimientoAeronave(models.Model):

    class Tipo(models.TextChoices):
        PREVENTIVO = 'preventivo', 'Preventivo'
        CORRECTIVO = 'correctivo', 'Correctivo'
        REVISION   = 'revision',   'Revisión Periódica'

    class Estado(models.TextChoices):
        PROGRAMADO = 'programado', 'Programado'
        EN_PROCESO = 'en_proceso', 'En Proceso'
        COMPLETADO = 'completado', 'Completado'
        CANCELADO  = 'cancelado',  'Cancelado'

    aeronave            = models.ForeignKey(Aeronave, on_delete=models.PROTECT, related_name='mantenimientos')
    tipo                = models.CharField(max_length=15, choices=Tipo.choices)
    estado              = models.CharField(max_length=15, choices=Estado.choices, default=Estado.PROGRAMADO)
    descripcion         = models.TextField()
    fecha_inicio        = models.DateField()
    fecha_fin_estimada  = models.DateField()
    fecha_fin_real      = models.DateField(null=True, blank=True)
    tecnico_responsable = models.CharField(max_length=200, blank=True)
    costo               = models.DecimalField(max_digits=12, decimal_places=2, null=True, blank=True)
    creado_en           = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name        = 'Mantenimiento de Aeronave'
        verbose_name_plural = 'Mantenimientos de Aeronave'
        ordering            = ['-fecha_inicio']

    def __str__(self):
        return f'{self.get_tipo_display()} — {self.aeronave} ({self.estado})'
