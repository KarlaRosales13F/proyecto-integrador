from rest_framework import viewsets
from rest_framework.filters import OrderingFilter, SearchFilter

from vuelos.models import Pasajero
from vuelos.pagination import StandardPagination
from vuelos.permissions import EsStaffOSoloLectura
from vuelos.serializers import PasajeroSerializer


class PasajeroViewSet(viewsets.ModelViewSet):
    queryset = Pasajero.objects.select_related("usuario").all()
    serializer_class = PasajeroSerializer
    permission_classes = [EsStaffOSoloLectura]
    pagination_class = StandardPagination
    filter_backends = [SearchFilter, OrderingFilter]
    search_fields = ["numero_pasaporte", "nacionalidad", "usuario__first_name", "usuario__last_name"]
    ordering_fields = ["usuario__last_name", "nacionalidad"]
