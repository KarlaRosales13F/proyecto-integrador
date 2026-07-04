from django.db import models
from .aeropuerto import Aeropuerto
from .aeronave   import Aeronave


class Vuelo(models.Model):

    class Estado(models.TextChoices):
        PROGRAMADO  = 'programado',  'Programado'
        ABORDANDO   = 'abordando',   'Abordando'
        DESPEGADO   = 'despegado',   'Despegado'
        ATERRIZADO  = 'aterrizado',  'Aterrizado'
        CANCELADO   = 'cancelado',   'Cancelado'

    origen        = models.ForeignKey(Aeropuerto, on_delete=models.PROTECT, related_name='vuelos_origen')
    destino       = models.ForeignKey(Aeropuerto, on_delete=models.PROTECT, related_name='vuelos_destino')
    aeronave      = models.ForeignKey(Aeronave,   on_delete=models.PROTECT, related_name='vuelos')
    fecha_salida  = models.DateTimeField()
    fecha_llegada = models.DateTimeField()
    estado        = models.CharField(max_length=20, choices=Estado.choices, default=Estado.PROGRAMADO)
    precio        = models.DecimalField(max_digits=10, decimal_places=2)

    class Meta:
        verbose_name        = 'Vuelo'
        verbose_name_plural = 'Vuelos'
        ordering            = ['fecha_salida']

    def __str__(self):
        return f'{self.origen.codigo_iata} → {self.destino.codigo_iata} | {self.fecha_salida:%d/%m/%Y %H:%M}'
    
    @property
    def precio_con_impuesto(self):
        return round(float(self.precio) * 1.12, 2)

    @property
    def asientos_disponibles(self):
        ocupados = self.reservas.filter(estado='confirmada').count()
        return self.aeronave.capacidad - ocupados