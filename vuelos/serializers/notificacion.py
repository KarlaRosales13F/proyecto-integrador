from rest_framework import serializers
from vuelos.models import Notificacion

class NotificacionSerializer(serializers.ModelSerializer):
    class Meta:
        model  = Notificacion
        fields = ['id', 'usuario', 'tipo', 'titulo', 'mensaje', 'leida', 'fecha']
        read_only_fields = ['fecha']
