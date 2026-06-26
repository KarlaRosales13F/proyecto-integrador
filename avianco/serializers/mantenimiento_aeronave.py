from rest_framework import serializers
from vuelos.models import MantenimientoAeronave

class MantenimientoAeronaveSerializer(serializers.ModelSerializer):
    class Meta:
        model  = MantenimientoAeronave
        fields = [
            'id', 'aeronave', 'tipo', 'estado', 'descripcion',
            'fecha_inicio', 'fecha_fin_estimada', 'fecha_fin_real',
            'tecnico_responsable', 'costo', 'creado_en'
        ]
        read_only_fields = ['creado_en']
