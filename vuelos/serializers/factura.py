from rest_framework import serializers
from vuelos.models import Factura


class FacturaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Factura
        fields = ['id', 'reserva', 'total', 'impuestos', 'estado', 'fecha']
        read_only_fields = ['fecha']
