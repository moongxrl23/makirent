"""URLs principales del proyecto."""
from django.urls import path, include

urlpatterns = [
    # Todo lo de la app (páginas y API) se define en maquinaria/urls.py
    path("", include("maquinaria.urls")),
]

# Manejador del error 404 controlado (usa maquinaria.views.error_404).
# Django lo activa solo cuando DEBUG = False.
handler404 = "maquinaria.views.error_404"
