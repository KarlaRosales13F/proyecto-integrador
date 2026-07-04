from rest_framework import serializers
from vuelos.models import TipoAvion

class TipoAvionSerializer(serializers.ModelSerializer):
    class Meta:
        model  = TipoAvion
        fields = ['id', 'nombre', 'fabricante', 'autonomia_km', 'descripcion']
