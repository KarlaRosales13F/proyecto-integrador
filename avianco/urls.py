from django.urls import include, path
from rest_framework.routers import DefaultRouter

from .views import (
    AsignacionTripulacionViewSet,
    CheckInViewSet,
    DocumentoPasajeroViewSet,
    FeedbackPasajeroViewSet,
    MantenimientoAeronaveViewSet,
    PromocionViewSet,
    SolicitudServicioViewSet,
    TripulacionViewSet,
)

router = DefaultRouter()
router.register(r"asignaciones-tripulacion", AsignacionTripulacionViewSet, basename="asignacion-tripulacion")
router.register(r"checkins",                 CheckInViewSet,               basename="checkin")
router.register(r"documentos-pasajero",      DocumentoPasajeroViewSet,     basename="documento-pasajero")
router.register(r"feedbacks-pasajero",       FeedbackPasajeroViewSet,      basename="feedback-pasajero")
router.register(r"mantenimientos-aeronave",  MantenimientoAeronaveViewSet, basename="mantenimiento-aeronave")
router.register(r"promociones",              PromocionViewSet,             basename="promocion")
router.register(r"solicitudes-servicio",     SolicitudServicioViewSet,     basename="solicitud-servicio")
router.register(r"tripulaciones",            TripulacionViewSet,           basename="tripulacion")

urlpatterns = [
    path("", include(router.urls)),
]
