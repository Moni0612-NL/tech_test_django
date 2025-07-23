from django.contrib.auth.models import AbstractUser
from django.db import models


# Extendemos el modelo de usuario base de Django
class Usuario(AbstractUser):
    email = models.EmailField(unique=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    # Opcional: para mostrar nombre completo en admin
    def __str__(self):
        return f"{self.first_name} {self.last_name} ({self.email})"


# Modelo Ingreso
class Ingreso(models.Model):
    usuario = models.ForeignKey(
        Usuario, on_delete=models.CASCADE, related_name="ingresos"
    )
    fecha_entrada = models.DateTimeField()
    fecha_salida = models.DateTimeField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"Ingreso de {self.usuario.email} el {self.fecha_entrada}"
