from rest_framework import viewsets
from rest_framework.filters import SearchFilter, OrderingFilter
from django_filters.rest_framework import DjangoFilterBackend
from vuelos.models import CheckIn
from vuelos.serializers import CheckInSerializer
from vuelos.pagination import StandardPagination
from vuelos.permissions import EsStaffOSoloLectura

class CheckInViewSet(viewsets.ModelViewSet):
    queryset           = CheckIn.objects.select_related('reserva').all()
    serializer_class   = CheckInSerializer
    permission_classes = [EsStaffOSoloLectura]
    pagination_class   = StandardPagination
    filter_backends    = [DjangoFilterBackend, SearchFilter, OrderingFilter]
    filterset_fields   = ['reserva', 'metodo', 'equipaje_listo']
    search_fields      = ['asiento_final', 'pase_abordar']
    ordering_fields    = ['fecha_checkin', 'metodo']
