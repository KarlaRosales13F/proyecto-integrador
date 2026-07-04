from rest_framework import viewsets
from rest_framework.filters import OrderingFilter
from django_filters.rest_framework import DjangoFilterBackend
from vuelos.models import CheckIn
from vuelos.serializers.checkin import CheckInSerializer
from vuelos.pagination import StandardPagination
from vuelos.permissions import EsStaffOSoloLectura


class CheckInViewSet(viewsets.ModelViewSet):
    queryset           = CheckIn.objects.select_related('reserva').all()
    serializer_class   = CheckInSerializer
    permission_classes = [EsStaffOSoloLectura]
    pagination_class   = StandardPagination
    filter_backends    = [DjangoFilterBackend, OrderingFilter]
    filterset_fields   = ['estado', 'reserva']
    ordering_fields    = ['-hora_checkin']
