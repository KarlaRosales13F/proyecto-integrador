from rest_framework import viewsets
from rest_framework.filters import SearchFilter, OrderingFilter
from vuelos.models import TipoAvion
from vuelos.serializers import TipoAvionSerializer
from vuelos.pagination import StandardPagination
from vuelos.permissions import EsStaffOSoloLectura

class TipoAvionViewSet(viewsets.ModelViewSet):
    queryset           = TipoAvion.objects.all()
    serializer_class   = TipoAvionSerializer
    permission_classes = [EsStaffOSoloLectura]
    pagination_class   = StandardPagination
    filter_backends    = [SearchFilter, OrderingFilter]
    search_fields      = ['nombre', 'fabricante']
    ordering_fields    = ['nombre', 'fabricante']
