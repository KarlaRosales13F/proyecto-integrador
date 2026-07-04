from rest_framework import viewsets
from rest_framework.filters import SearchFilter, OrderingFilter
from django_filters.rest_framework import DjangoFilterBackend
from vuelos.models import Puerta
from vuelos.serializers import PuertaSerializer
from vuelos.pagination import StandardPagination
from vuelos.permissions import EsStaffOSoloLectura

class PuertaViewSet(viewsets.ModelViewSet):
    queryset           = Puerta.objects.select_related('terminal').all()
    serializer_class   = PuertaSerializer
    permission_classes = [EsStaffOSoloLectura]
    pagination_class   = StandardPagination
    filter_backends    = [DjangoFilterBackend, SearchFilter, OrderingFilter]
    filterset_fields   = ['terminal', 'activa']
    search_fields      = ['codigo', 'terminal__nombre']
    ordering_fields    = ['codigo']
