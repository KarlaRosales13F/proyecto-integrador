from rest_framework import serializers
from vuelos.models import Pago

class PagoSerializer(serializers.ModelSerializer):
    class Meta:
        model  = Pago
        fields = ['id', 'reserva', 'metodo_pago', 'monto', 'estado', 'referencia', 'fecha']
        read_only_fields = ['fecha']
