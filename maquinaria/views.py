"""Vistas HTML (100% templates) y manejador del 404."""
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import TemplateView, ListView, CreateView, UpdateView, DeleteView
from .models import Maquina, Cliente, Arriendo
from .forms import MaquinaForm, ClienteForm, ArriendoForm


class InicioView(TemplateView):
    """Landing page. Al definir la raíz '/', se elimina el 404 del root."""
    template_name = "maquinaria/inicio.html"

    def get_context_data(self, **kwargs):
        ctx = super().get_context_data(**kwargs)
        ctx["destacadas"] = Maquina.objects.filter(disponible=True)[:3]
        return ctx


class ContactoView(TemplateView):
    template_name = "maquinaria/contacto.html"


# ---------- Máquinas ----------
class MaquinaList(ListView):
    model = Maquina
    template_name = "maquinaria/maquinas.html"
    context_object_name = "maquinas"


class MaquinaCreate(CreateView):
    model = Maquina
    form_class = MaquinaForm
    template_name = "maquinaria/formulario.html"
    success_url = reverse_lazy("maquinas")
    extra_context = {"titulo": "Nueva máquina", "volver": "maquinas"}


class MaquinaUpdate(UpdateView):
    model = Maquina
    form_class = MaquinaForm
    template_name = "maquinaria/formulario.html"
    success_url = reverse_lazy("maquinas")
    extra_context = {"titulo": "Editar máquina", "volver": "maquinas"}


class MaquinaDelete(DeleteView):
    model = Maquina
    template_name = "maquinaria/confirmar_eliminar.html"
    success_url = reverse_lazy("maquinas")


# ---------- Clientes ----------
class ClienteList(ListView):
    model = Cliente
    template_name = "maquinaria/clientes.html"
    context_object_name = "clientes"


class ClienteCreate(CreateView):
    model = Cliente
    form_class = ClienteForm
    template_name = "maquinaria/formulario.html"
    success_url = reverse_lazy("clientes")
    extra_context = {"titulo": "Nuevo cliente", "volver": "clientes"}


class ClienteUpdate(UpdateView):
    model = Cliente
    form_class = ClienteForm
    template_name = "maquinaria/formulario.html"
    success_url = reverse_lazy("clientes")
    extra_context = {"titulo": "Editar cliente", "volver": "clientes"}


class ClienteDelete(DeleteView):
    model = Cliente
    template_name = "maquinaria/confirmar_eliminar.html"
    success_url = reverse_lazy("clientes")


# ---------- Arriendos ----------
class ArriendoList(ListView):
    model = Arriendo
    template_name = "maquinaria/arriendos.html"
    context_object_name = "arriendos"


class ArriendoCreate(CreateView):
    model = Arriendo
    form_class = ArriendoForm
    template_name = "maquinaria/formulario.html"
    success_url = reverse_lazy("arriendos")
    extra_context = {"titulo": "Nuevo arriendo", "volver": "arriendos"}


class ArriendoUpdate(UpdateView):
    model = Arriendo
    form_class = ArriendoForm
    template_name = "maquinaria/formulario.html"
    success_url = reverse_lazy("arriendos")
    extra_context = {"titulo": "Editar arriendo", "volver": "arriendos"}


class ArriendoDelete(DeleteView):
    model = Arriendo
    template_name = "maquinaria/confirmar_eliminar.html"
    success_url = reverse_lazy("arriendos")


# ---------- Error 404 controlado ----------
def error_404(request, exception):
    """Muestra 'esta página no existe' con botón para volver al inicio."""
    return render(request, "maquinaria/404.html", status=404)
