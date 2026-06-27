from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import viewsets
from rest_framework.filters import OrderingFilter, SearchFilter

from vuelos.models import Ciudad
from vuelos.pagination import StandardPagination
from vuelos.permissions import EsStaffOSoloLectura
from vuelos.serializers import CiudadSerializer


class CiudadViewSet(viewsets.ModelViewSet):
    queryset = Ciudad.objects.select_related("pais").all()
    serializer_class = CiudadSerializer
    permission_classes = [EsStaffOSoloLectura]
    pagination_class = StandardPagination
    filter_backends = [DjangoFilterBackend, SearchFilter, OrderingFilter]
    filterset_fields = ["pais"]
    search_fields = ["nombre", "pais__nombre"]
    ordering_fields = ["nombre"]
