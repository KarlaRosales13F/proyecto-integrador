from django.urls import include, path
from rest_framework.routers import DefaultRouter
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

from .views import (
    AeronaveViewSet,
    AeropuertoViewSet,
    CiudadViewSet,
    LogoutView,
    PaisViewSet,
    PasajeroViewSet,
    PuertaViewSet,
    RegisterView,
    ReservaViewSet,
    TerminalViewSet,
    VueloViewSet,
    health_check,
)

router = DefaultRouter()
router.register(r"aeropuertos", AeropuertoViewSet, basename="aeropuerto")
router.register(r"aeronaves", AeronaveViewSet, basename="aeronave")
router.register(r"vuelos", VueloViewSet, basename="vuelo")
router.register(r"pasajeros", PasajeroViewSet, basename="pasajero")
router.register(r"reservas", ReservaViewSet, basename="reserva")
router.register(r"paises", PaisViewSet, basename="pais")
router.register(r"ciudades", CiudadViewSet, basename="ciudad")
router.register(r"terminales", TerminalViewSet, basename="terminal")
router.register(r"puertas", PuertaViewSet, basename="puerta")

urlpatterns = [
    path("health/", health_check, name="health-check"),
    path("auth/register/", RegisterView.as_view(), name="register"),
    path("auth/logout/", LogoutView.as_view(), name="logout"),
    path("auth/token/", TokenObtainPairView.as_view(), name="token_obtain_pair"),
    path("auth/token/refresh/", TokenRefreshView.as_view(), name="token_refresh"),
    path("", include(router.urls)),
]
