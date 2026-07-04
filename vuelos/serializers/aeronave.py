from rest_framework import serializers
from vuelos.models import Aeronave


class AeronaveSerializer(serializers.ModelSerializer):
    class Meta:
        model  = Aeronave
        fields = ['id', 'matricula', 'modelo', 'capacidad']