from rest_framework import serializers
from vuelos.models import Aeropuerto


class AeropuertoSerializer(serializers.ModelSerializer):
    class Meta:
        model  = Aeropuerto
        fields = ['id', 'codigo_iata', 'nombre', 'ciudad', 'pais']