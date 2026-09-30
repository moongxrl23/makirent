"""Endpoints de la API REST (ViewSets = CRUD completo automático)."""
from rest_framework import viewsets
from .models import Maquina, Cliente, Arriendo
from .serializers import MaquinaSerializer, ClienteSerializer, ArriendoSerializer


class MaquinaViewSet(viewsets.ModelViewSet):
    queryset = Maquina.objects.all()
    serializer_class = MaquinaSerializer


class ClienteViewSet(viewsets.ModelViewSet):
    queryset = Cliente.objects.all()
    serializer_class = ClienteSerializer


class ArriendoViewSet(viewsets.ModelViewSet):
    queryset = Arriendo.objects.select_related("cliente", "maquina")
    serializer_class = ArriendoSerializer
