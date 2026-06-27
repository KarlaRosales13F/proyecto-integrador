from django.db.models import Count
from django.db.models.deletion import ProtectedError
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import status, viewsets
from rest_framework.decorators import action
from rest_framework.filters import OrderingFilter, SearchFilter
from rest_framework.response import Response

from vuelos.models import Aeropuerto
from vuelos.pagination import StandardPagination
from vuelos.permissions import EsStaffOSoloLectura
from vuelos.serializers import AeropuertoSerializer


class AeropuertoViewSet(viewsets.ModelViewSet):
    queryset = Aeropuerto.objects.all()
    serializer_class = AeropuertoSerializer
    permission_classes = [EsStaffOSoloLectura]
    pagination_class = StandardPagination
    filter_backends = [DjangoFilterBackend, SearchFilter, OrderingFilter]
    filterset_fields = ["pais"]
    search_fields = ["codigo_iata", "nombre", "ciudad", "pais"]
    ordering_fields = ["codigo_iata", "pais", "ciudad"]

    def destroy(self, request, *args, **kwargs):
        try:
            return super().destroy(request, *args, **kwargs)
        except ProtectedError:
            return Response({"error": "No se puede eliminar porque tiene registros asociados."}, status=status.HTTP_400_BAD_REQUEST)

    @action(detail=False, methods=["get"], url_path="estadisticas")
    def estadisticas(self, request):
        qs = Aeropuerto.objects.all()
        return Response({
            "total": qs.count(),
            "por_pais": list(qs.values("pais").annotate(total=Count("id")).order_by("-total")),
        })
