from rest_framework import viewsets
from rest_framework.filters import SearchFilter, OrderingFilter
from vuelos.models import Pais
from vuelos.serializers import PaisSerializer
from vuelos.pagination import StandardPagination
from vuelos.permissions import EsStaffOSoloLectura

class PaisViewSet(viewsets.ModelViewSet):
    queryset           = Pais.objects.all()
    serializer_class   = PaisSerializer
    permission_classes = [EsStaffOSoloLectura]
    pagination_class   = StandardPagination
    filter_backends    = [SearchFilter, OrderingFilter]
    search_fields      = ['nombre', 'codigo']
    ordering_fields    = ['nombre', 'codigo']
