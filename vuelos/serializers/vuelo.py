from rest_framework import serializers
from vuelos.models import Vuelo
from .aeropuerto import AeropuertoSerializer
from .aeronave   import AeronaveSerializer


class VueloSerializer(serializers.ModelSerializer):
    origen_detalle  = AeropuertoSerializer(source='origen',   read_only=True)
    destino_detalle = AeropuertoSerializer(source='destino',  read_only=True)
    aeronave_detalle = AeronaveSerializer(source='aeronave',  read_only=True)

    class Meta:
        model  = Vuelo
        fields = [
            'id', 'origen', 'destino', 'aeronave',
            'origen_detalle', 'destino_detalle', 'aeronave_detalle',
            'fecha_salida', 'fecha_llegada', 'estado', 'precio',
        ]