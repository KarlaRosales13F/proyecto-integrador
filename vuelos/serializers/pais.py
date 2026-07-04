from rest_framework import serializers
from vuelos.models import Pais

class PaisSerializer(serializers.ModelSerializer):
    class Meta:
        model  = Pais
        fields = ['id', 'nombre', 'codigo', 'bandera']
