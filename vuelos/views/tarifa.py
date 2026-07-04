from rest_framework import viewsets
from rest_framework.filters import SearchFilter, OrderingFilter
from django_filters.rest_framework import DjangoFilterBackend
from vuelos.models import Tarifa
from vuelos.serializers import TarifaSerializer
from vuelos.pagination import StandardPagination
from vuelos.permissions import EsStaffOSoloLectura

class TarifaViewSet(viewsets.ModelViewSet):
    queryset           = Tarifa.objects.all()
    serializer_class   = TarifaSerializer
    permission_classes = [EsStaffOSoloLectura]
    pagination_class   = StandardPagination
    filter_backends    = [DjangoFilterBackend, SearchFilter, OrderingFilter]
    filterset_fields   = ['clase']
    search_fields      = ['nombre', 'clase']
    ordering_fields    = ['nombre', 'clase', 'descuento']
