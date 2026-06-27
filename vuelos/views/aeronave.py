from django.db.models import Avg, Max, Min
from django.db.models.deletion import ProtectedError
from rest_framework import status, viewsets
from rest_framework.decorators import action
from rest_framework.filters import OrderingFilter, SearchFilter
from rest_framework.response import Response

from vuelos.models import Aeronave
from vuelos.pagination import StandardPagination
from vuelos.permissions import EsStaffOSoloLectura
from vuelos.serializers import AeronaveSerializer


class AeronaveViewSet(viewsets.ModelViewSet):
    queryset = Aeronave.objects.all()
    serializer_class = AeronaveSerializer
    permission_classes = [EsStaffOSoloLectura]
    pagination_class = StandardPagination
    filter_backends = [SearchFilter, OrderingFilter]
    search_fields = ["matricula", "modelo"]
    ordering_fields = ["modelo", "capacidad"]

    def destroy(self, request, *args, **kwargs):
        try:
            return super().destroy(request, *args, **kwargs)
        except ProtectedError:
            return Response({"error": "No se puede eliminar porque tiene vuelos asociados."}, status=status.HTTP_400_BAD_REQUEST)

    @action(detail=False, methods=["get"], url_path="estadisticas")
    def estadisticas(self, request):
        qs = Aeronave.objects.all()
        return Response({
            "total": qs.count(),
            "capacidad_promedio": round(qs.aggregate(Avg("capacidad"))["capacidad__avg"] or 0, 0),
            "capacidad_maxima": qs.aggregate(Max("capacidad"))["capacidad__max"],
            "capacidad_minima": qs.aggregate(Min("capacidad"))["capacidad__min"],
        })
