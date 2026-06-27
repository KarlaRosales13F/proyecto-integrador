from django.db.models import Avg
from django.db.models.deletion import ProtectedError
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import status, viewsets
from rest_framework.decorators import action
from rest_framework.filters import OrderingFilter, SearchFilter
from rest_framework.permissions import IsAdminUser
from rest_framework.response import Response

from vuelos.models import Vuelo
from vuelos.pagination import StandardPagination
from vuelos.permissions import EsStaffOSoloLectura
from vuelos.serializers import VueloSerializer


class VueloViewSet(viewsets.ModelViewSet):
    queryset = Vuelo.objects.select_related("origen", "destino", "aeronave").all()
    serializer_class = VueloSerializer
    permission_classes = [EsStaffOSoloLectura]
    pagination_class = StandardPagination
    filter_backends = [DjangoFilterBackend, SearchFilter, OrderingFilter]
    filterset_fields = ["estado", "origen", "destino"]
    search_fields = ["origen__codigo_iata", "destino__codigo_iata"]
    ordering_fields = ["fecha_salida", "precio"]

    def destroy(self, request, *args, **kwargs):
        try:
            return super().destroy(request, *args, **kwargs)
        except ProtectedError:
            return Response({"error": "No se puede eliminar el vuelo porque tiene reservas asociadas."}, status=status.HTTP_400_BAD_REQUEST)

    @action(detail=True, methods=["post"], permission_classes=[IsAdminUser], url_path="cancelar")
    def cancelar(self, request, pk=None):
        vuelo = self.get_object()
        if vuelo.estado == "cancelado":
            return Response({"error": "El vuelo ya está cancelado."}, status=status.HTTP_400_BAD_REQUEST)
        vuelo.estado = "cancelado"
        vuelo.save(update_fields=["estado"])
        return Response({"mensaje": "Vuelo cancelado.", "estado": vuelo.estado})

    @action(detail=True, methods=["get"], url_path="asientos-disponibles")
    def asientos_disponibles(self, request, pk=None):
        vuelo = self.get_object()
        return Response({
            "vuelo_id": vuelo.id,
            "capacidad_total": vuelo.aeronave.capacidad,
            "asientos_disponibles": vuelo.asientos_disponibles,
            "asientos_ocupados": vuelo.aeronave.capacidad - vuelo.asientos_disponibles,
        })

    @action(detail=False, methods=["get"], url_path="disponibles")
    def disponibles(self, request):
        qs = self.filter_queryset(self.get_queryset().filter(estado="programado"))
        page = self.paginate_queryset(qs)
        if page is not None:
            return self.get_paginated_response(VueloSerializer(page, many=True).data)
        return Response(VueloSerializer(qs, many=True).data)

    @action(detail=False, methods=["get"], url_path="estadisticas")
    def estadisticas(self, request):
        qs = Vuelo.objects.all()
        return Response({
            "total": qs.count(),
            "programados": qs.filter(estado="programado").count(),
            "cancelados": qs.filter(estado="cancelado").count(),
            "precio_promedio": round(float(qs.aggregate(Avg("precio"))["precio__avg"] or 0), 2),
        })
