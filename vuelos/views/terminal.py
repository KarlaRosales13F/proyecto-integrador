from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import viewsets
from rest_framework.filters import OrderingFilter, SearchFilter

from vuelos.models import Terminal
from vuelos.pagination import StandardPagination
from vuelos.permissions import EsStaffOSoloLectura
from vuelos.serializers import TerminalSerializer


class TerminalViewSet(viewsets.ModelViewSet):
    queryset = Terminal.objects.select_related("aeropuerto").all()
    serializer_class = TerminalSerializer
    permission_classes = [EsStaffOSoloLectura]
    pagination_class = StandardPagination
    filter_backends = [DjangoFilterBackend, SearchFilter, OrderingFilter]
    filterset_fields = ["aeropuerto"]
    search_fields = ["nombre", "aeropuerto__nombre"]
    ordering_fields = ["nombre"]
