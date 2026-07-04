from rest_framework import serializers
from vuelos.models import MetodoPago

class MetodoPagoSerializer(serializers.ModelSerializer):
    class Meta:
        model  = MetodoPago
        fields = ['id', 'nombre', 'tipo', 'activo']
