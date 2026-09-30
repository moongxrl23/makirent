"""Rutas de la app: páginas HTML + API REST bajo /api/."""
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from . import views
from .api_views import MaquinaViewSet, ClienteViewSet, ArriendoViewSet

# El router genera automáticamente /api/maquinas/, /api/clientes/, etc.
router = DefaultRouter()
router.register("maquinas", MaquinaViewSet)
router.register("clientes", ClienteViewSet)
router.register("arriendos", ArriendoViewSet)

urlpatterns = [
    path("", views.InicioView.as_view(), name="inicio"),
    path("contacto/", views.ContactoView.as_view(), name="contacto"),

    path("maquinas/", views.MaquinaList.as_view(), name="maquinas"),
    path("maquinas/nueva/", views.MaquinaCreate.as_view(), name="maquina_nueva"),
    path("maquinas/<int:pk>/editar/", views.MaquinaUpdate.as_view(), name="maquina_editar"),
    path("maquinas/<int:pk>/eliminar/", views.MaquinaDelete.as_view(), name="maquina_eliminar"),

    path("clientes/", views.ClienteList.as_view(), name="clientes"),
    path("clientes/nuevo/", views.ClienteCreate.as_view(), name="cliente_nuevo"),
    path("clientes/<int:pk>/editar/", views.ClienteUpdate.as_view(), name="cliente_editar"),
    path("clientes/<int:pk>/eliminar/", views.ClienteDelete.as_view(), name="cliente_eliminar"),

    path("arriendos/", views.ArriendoList.as_view(), name="arriendos"),
    path("arriendos/nuevo/", views.ArriendoCreate.as_view(), name="arriendo_nuevo"),
    path("arriendos/<int:pk>/editar/", views.ArriendoUpdate.as_view(), name="arriendo_editar"),
    path("arriendos/<int:pk>/eliminar/", views.ArriendoDelete.as_view(), name="arriendo_eliminar"),

    path("api/", include(router.urls)),
]
