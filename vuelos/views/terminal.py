from rest_framework import viewsets
from rest_framework.filters import SearchFilter, OrderingFilter
from django_filters.rest_framework import DjangoFilterBackend
from vuelos.models import Terminal
from vuelos.serializers import TerminalSerializer
from vuelos.pagination import StandardPagination
from vuelos.permissions import EsStaffOSoloLectura

class TerminalViewSet(viewsets.ModelViewSet):
    queryset           = Terminal.objects.select_related('aeropuerto').all()
    serializer_class   = TerminalSerializer
    permission_classes = [EsStaffOSoloLectura]
    pagination_class   = StandardPagination
    filter_backends    = [DjangoFilterBackend, SearchFilter, OrderingFilter]
    filterset_fields   = ['aeropuerto']
    search_fields      = ['nombre', 'aeropuerto__nombre']
    ordering_fields    = ['nombre']
