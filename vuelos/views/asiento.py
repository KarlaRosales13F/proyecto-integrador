from rest_framework import viewsets
from rest_framework.filters import SearchFilter, OrderingFilter
from django_filters.rest_framework import DjangoFilterBackend
from vuelos.models import Asiento
from vuelos.serializers.asiento import AsientoSerializer
from vuelos.pagination import StandardPagination
from vuelos.permissions import EsStaffOSoloLectura


class AsientoViewSet(viewsets.ModelViewSet):
    queryset           = Asiento.objects.select_related('vuelo').all()
    serializer_class   = AsientoSerializer
    permission_classes = [EsStaffOSoloLectura]
    pagination_class   = StandardPagination
    filter_backends    = [DjangoFilterBackend, SearchFilter, OrderingFilter]
    filterset_fields   = ['vuelo', 'clase', 'disponible']
    search_fields      = ['codigo', 'clase']
    ordering_fields    = ['fila', 'columna', 'clase']
