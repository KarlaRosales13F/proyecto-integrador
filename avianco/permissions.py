from rest_framework.permissions import BasePermission, SAFE_METHODS


class EsStaffOSoloLectura(BasePermission):
    """Staff puede todo, usuarios autenticados solo leer."""

    def has_permission(self, request, view):
        if request.method in SAFE_METHODS:
            return request.user and request.user.is_authenticated
        return request.user and request.user.is_staff