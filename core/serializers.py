from rest_framework import serializers

from .models import Ingreso, Usuario


class UsuarioSerializer(serializers.ModelSerializer):
    class Meta:
        model = Usuario
        fields = [
            "id",
            "username",
            "email",
            "first_name",
            "last_name",
            "password",
            "created_at",
            "updated_at",
        ]
        extra_kwargs = {
            "password": {"write_only": True, "required": False},
            "created_at": {"read_only": True},
            "updated_at": {"read_only": True},
        }

    def create(self, validated_data):
        password = validated_data.pop("password", None)
        user = Usuario(**validated_data)
        if password:
            user.set_password(password)
        user.save()
        return user

    def update(self, instance, validated_data):
        password = validated_data.pop("password", None)
        for attr, value in validated_data.items():
            setattr(instance, attr, value)
        if password:
            instance.set_password(password)
        instance.save()
        return instance


class IngresoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Ingreso
        fields = "__all__"
        read_only_fields = ("created_at", "updated_at")
