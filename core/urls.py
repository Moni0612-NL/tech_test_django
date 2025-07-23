from django.urls import path

from .views import (UsuarioCreateAPIView, actualizar_usuario, crear_ingreso,
                    eliminar_usuario)

urlpatterns = [
    path("usuarios/", UsuarioCreateAPIView.as_view(), name="usuario-create"),
    path("ingresos/", crear_ingreso, name="crear_ingreso"),
    path(
        "usuarios/<int:usuario_id>/eliminar/", eliminar_usuario, name="usuario-delete"
    ),
    path("usuarios/<int:usuario_id>/", actualizar_usuario, name="actualizar_usuario"),
]
