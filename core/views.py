from datetime import timedelta

from django.utils import timezone
from rest_framework import generics, status
from rest_framework.decorators import api_view
from rest_framework.response import Response

from .models import Ingreso, Usuario
from .serializers import IngresoSerializer, UsuarioSerializer


# Vista basada en clase
class UsuarioCreateAPIView(generics.CreateAPIView):
    queryset = Usuario.objects.all()
    serializer_class = UsuarioSerializer


# Vista basada en función para crear un usuario
@api_view(["POST"])
def crear_usuario(request):
    serializer = UsuarioSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

# vista basada en funcion para editar un usuario
@api_view(["PUT"])
def actualizar_usuario(request, usuario_id):
    try:
        usuario = Usuario.objects.get(id=usuario_id)
    except Usuario.DoesNotExist:
        return Response(
            {"error": "Usuario no encontrado."}, status=status.HTTP_404_NOT_FOUND
        )

    serializer = UsuarioSerializer(usuario, data=request.data, partial=True)
    if serializer.is_valid():
        serializer.save()
        return Response(
            {
                "mensaje": "Usuario actualizado correctamente.",
                "usuario": serializer.data,
            }
        )
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

# vista para eliminar
@api_view(["DELETE"])
def eliminar_usuario(request, usuario_id):
    try:
        usuario = Usuario.objects.get(id=usuario_id)
    except Usuario.DoesNotExist:
        return Response(
            {"error": "Usuario no encontrado."}, status=status.HTTP_404_NOT_FOUND
        )

    usuario.delete()
    return Response(
        {"mensaje": "Usuario eliminado correctamente."}, status=status.HTTP_200_OK
    )

# vista para crear un ingreso
@api_view(["POST"])
def crear_ingreso(request):
    usuario_id = request.data.get("usuario_id")

    if not usuario_id:
        return Response(
            {"error": "El campo usuario_id es requerido."},
            status=status.HTTP_400_BAD_REQUEST,
        )

    try:
        usuario = Usuario.objects.get(id=usuario_id)
    except Usuario.DoesNotExist:
        return Response(
            {"error": "Usuario no encontrado."}, status=status.HTTP_404_NOT_FOUND
        )

    fecha_entrada = timezone.now()
    fecha_salida = fecha_entrada + timedelta(hours=5)

    ingreso = Ingreso.objects.create(
        usuario=usuario, fecha_entrada=fecha_entrada, fecha_salida=fecha_salida
    )

    serializer = IngresoSerializer(ingreso)
    return Response(serializer.data, status=status.HTTP_201_CREATED)
