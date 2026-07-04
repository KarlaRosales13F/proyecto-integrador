from rest_framework import viewsets
from rest_framework.filters import SearchFilter, OrderingFilter
from django_filters.rest_framework import DjangoFilterBackend
from vuelos.models import Tripulacion
from vuelos.serializers import TripulacionSerializer
from vuelos.pagination import StandardPagination
from vuelos.permissions import EsStaffOSoloLectura

class TripulacionViewSet(viewsets.ModelViewSet):
    queryset           = Tripulacion.objects.all()
    serializer_class   = TripulacionSerializer
    permission_classes = [EsStaffOSoloLectura]
    pagination_class   = StandardPagination
    filter_backends    = [DjangoFilterBackend, SearchFilter, OrderingFilter]
    filterset_fields   = ['rol', 'activo']
    search_fields      = ['nombre', 'apellido', 'licencia']
    ordering_fields    = ['apellido', 'nombre', 'rol']
