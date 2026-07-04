from rest_framework import viewsets
from rest_framework.filters import SearchFilter, OrderingFilter
from django_filters.rest_framework import DjangoFilterBackend
from vuelos.models import Aerolinea
from vuelos.serializers.aerolinea import AerolineaSerializer
from vuelos.pagination import StandardPagination
from vuelos.permissions import EsStaffOSoloLectura


class AerolineaViewSet(viewsets.ModelViewSet):
    queryset           = Aerolinea.objects.all()
    serializer_class   = AerolineaSerializer
    permission_classes = [EsStaffOSoloLectura]
    pagination_class   = StandardPagination
    filter_backends    = [DjangoFilterBackend, SearchFilter, OrderingFilter]
    filterset_fields   = ['pais']
    search_fields      = ['nombre', 'codigo', 'pais']
    ordering_fields    = ['nombre', 'codigo']
