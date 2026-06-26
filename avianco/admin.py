from django.contrib import admin
from vuelos.models import Aeropuerto, Aeronave, Vuelo, Pasajero, Reserva

admin.site.register(Aeropuerto)
admin.site.register(Aeronave)
admin.site.register(Vuelo)
admin.site.register(Pasajero)
admin.site.register(Reserva)