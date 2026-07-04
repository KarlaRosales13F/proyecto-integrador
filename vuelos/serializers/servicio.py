from rest_framework import serializers
from vuelos.models import Servicio, ReservaServicio


class ServicioSerializer(serializers.ModelSerializer):
    class Meta:
        model = Servicio
        fields = ['id', 'nombre', 'descripcion', 'precio', 'tipo']


class ReservaServicioSerializer(serializers.ModelSerializer):
    class Meta:
        model = ReservaServicio
        fields = ['id', 'reserva', 'servicio', 'cantidad', 'precio_aplicado']
