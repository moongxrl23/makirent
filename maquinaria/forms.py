"""Formularios HTML (ModelForm) para las páginas con templates."""
from django import forms
from .models import Maquina, Cliente, Arriendo


class MaquinaForm(forms.ModelForm):
    class Meta:
        model = Maquina
        fields = ["nombre", "categoria", "descripcion", "precio_dia", "disponible"]


class ClienteForm(forms.ModelForm):
    class Meta:
        model = Cliente
        fields = ["nombre", "rut", "email", "telefono"]


class ArriendoForm(forms.ModelForm):
    class Meta:
        model = Arriendo
        fields = ["cliente", "maquina", "fecha_inicio", "fecha_fin", "estado"]
        widgets = {  # selector de fecha nativo del navegador
            "fecha_inicio": forms.DateInput(attrs={"type": "date"}),
            "fecha_fin": forms.DateInput(attrs={"type": "date"}),
        }

    def clean(self):
        datos = super().clean()
        ini, fin = datos.get("fecha_inicio"), datos.get("fecha_fin")
        if ini and fin and fin < ini:
            raise forms.ValidationError("La fecha fin no puede ser anterior al inicio.")
        return datos
