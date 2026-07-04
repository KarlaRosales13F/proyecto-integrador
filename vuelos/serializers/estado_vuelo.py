from rest_framework import serializers
from vuelos.models import EstadoVuelo

class EstadoVueloSerializer(serializers.ModelSerializer):
    class Meta:
        model  = EstadoVuelo
        fields = ['id', 'vuelo', 'estado', 'descripcion', 'fecha']
        read_only_fields = ['fecha']
