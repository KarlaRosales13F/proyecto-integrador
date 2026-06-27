from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import viewsets
from rest_framework.filters import OrderingFilter, SearchFilter

from vuelos.models import Puerta
from vuelos.pagination import StandardPagination
from vuelos.permissions import EsStaffOSoloLectura
from vuelos.serializers import PuertaSerializer


class PuertaViewSet(viewsets.ModelViewSet):
    queryset = Puerta.objects.select_related("terminal").all()
    serializer_class = PuertaSerializer
    permission_classes = [EsStaffOSoloLectura]
    pagination_class = StandardPagination
    filter_backends = [DjangoFilterBackend, SearchFilter, OrderingFilter]
    filterset_fields = ["terminal", "activa"]
    search_fields = ["codigo", "terminal__nombre"]
    ordering_fields = ["codigo"]
