from rest_framework import serializers
from vuelos.models import Tarifa

class TarifaSerializer(serializers.ModelSerializer):
    class Meta:
        model  = Tarifa
        fields = ['id', 'nombre', 'clase', 'descripcion', 'descuento']
