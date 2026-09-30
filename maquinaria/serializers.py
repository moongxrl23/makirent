"""Serializers: convierten modelos a JSON y validan datos de la API."""
from rest_framework import serializers
from .models import Maquina, Cliente, Arriendo


class MaquinaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Maquina
        fields = "__all__"


class ClienteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cliente
        fields = "__all__"


class ArriendoSerializer(serializers.ModelSerializer):
    total = serializers.IntegerField(read_only=True)  # campo calculado

    class Meta:
        model = Arriendo
        fields = "__all__"

    def validate(self, datos):
        # La fecha de término no puede ser anterior a la de inicio
        if datos["fecha_fin"] < datos["fecha_inicio"]:
            raise serializers.ValidationError("La fecha fin no puede ser anterior al inicio.")
        return datos
