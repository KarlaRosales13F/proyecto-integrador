from rest_framework import serializers

from vuelos.models import Reserva


class ReservaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Reserva
        fields = ["id", "vuelo", "pasajero", "asiento", "estado", "fecha_reserva"]
        read_only_fields = ["fecha_reserva"]

    def validate(self, data):
        vuelo = data.get("vuelo", getattr(self.instance, "vuelo", None))
        asiento = data.get("asiento", getattr(self.instance, "asiento", None))
        queryset = Reserva.objects.filter(vuelo=vuelo, asiento=asiento)
        if self.instance:
            queryset = queryset.exclude(pk=self.instance.pk)
        if queryset.exists():
            raise serializers.ValidationError({"asiento": "Este asiento ya está ocupado."})
        return data
