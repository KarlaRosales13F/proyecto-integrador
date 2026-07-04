from rest_framework import serializers
from vuelos.models import Aerolinea


class AerolineaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Aerolinea
        fields = ['id', 'nombre', 'codigo', 'pais', 'sitio_web']
