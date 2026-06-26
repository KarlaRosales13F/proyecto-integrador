from rest_framework import serializers
from vuelos.models import Promocion

class PromocionSerializer(serializers.ModelSerializer):
    class Meta:
        model  = Promocion
        fields = ['id', 'codigo', 'descripcion', 'descuento', 'activa', 'fecha_inicio', 'fecha_fin']
