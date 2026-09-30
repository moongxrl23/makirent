"""Modelos: Maquina, Cliente y Arriendo."""
from django.db import models


class Maquina(models.Model):
    """Una máquina disponible para arriendo (ej: retroexcavadora)."""
    CATEGORIAS = [
        ("excavacion", "Excavación"),
        ("elevacion", "Elevación"),
        ("compactacion", "Compactación"),
        ("energia", "Generación de energía"),
    ]
    nombre = models.CharField(max_length=100)
    categoria = models.CharField(max_length=20, choices=CATEGORIAS)
    descripcion = models.TextField(blank=True)
    precio_dia = models.PositiveIntegerField(help_text="Valor por día en CLP")
    disponible = models.BooleanField(default=True)
    # URL de una foto de la máquina (ej: "img/retroexcavadora.jpg" si la
    # pones en maquinaria/static/img/, o un link externo https://...)
    imagen_url = models.CharField(max_length=300, blank=True)

    # Ícono de Bootstrap Icons según categoría (se usa si no hay imagen_url)
    ICONOS_CATEGORIA = {
        "excavacion": "bi-cone-striped",
        "elevacion": "bi-arrow-up-square",
        "compactacion": "bi-layers",
        "energia": "bi-lightning-charge-fill",
    }

    @property
    def icono(self):
        return self.ICONOS_CATEGORIA.get(self.categoria, "bi-gear-fill")

    def __str__(self):
        return self.nombre


class Cliente(models.Model):
    """Empresa o persona que arrienda maquinaria."""
    nombre = models.CharField(max_length=100)
    rut = models.CharField(max_length=12, unique=True)
    email = models.EmailField()
    telefono = models.CharField(max_length=20, blank=True)

    def __str__(self):
        return f"{self.nombre} ({self.rut})"


class Arriendo(models.Model):
    """Registro de un arriendo: relaciona un cliente con una máquina."""
    ESTADOS = [("activo", "Activo"), ("finalizado", "Finalizado")]
    cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE, related_name="arriendos")
    maquina = models.ForeignKey(Maquina, on_delete=models.CASCADE, related_name="arriendos")
    fecha_inicio = models.DateField()
    fecha_fin = models.DateField()
    estado = models.CharField(max_length=12, choices=ESTADOS, default="activo")

    @property
    def total(self):
        """Total a pagar = días (inclusive) x precio por día."""
        dias = (self.fecha_fin - self.fecha_inicio).days + 1
        return dias * self.maquina.precio_dia

    def __str__(self):
        return f"{self.maquina} → {self.cliente}"
