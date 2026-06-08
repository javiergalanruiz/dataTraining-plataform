from rest_framework import serializers
from .models import GPSPoint
from django.utils.dateparse import parse_datetime
from django.utils import timezone

class GPSPointSerializer(serializers.ModelSerializer):
    # Declaramos los campos explícitamente como CharField para que DRF 
    # no los rechace si la app del móvil los envía con comas o vacíos.
    lat = serializers.CharField()
    lon = serializers.CharField()
    speed = serializers.CharField(required=False, allow_blank=True, allow_null=True)
    timestamp = serializers.CharField()

    def validate_lat(self, value):
        if not value or str(value).strip() == "" or "null" in str(value).lower() or "variable" in str(value):
            return 0.0
        try:
            return float(str(value).replace(",", "."))
        except ValueError:
            raise serializers.ValidationError("Latitud no es un número válido.")

    def validate_lon(self, value):
        if not value or str(value).strip() == "" or "null" in str(value).lower() or "variable" in str(value):
            return 0.0
        try:
            return float(str(value).replace(",", "."))
        except ValueError:
            raise serializers.ValidationError("Longitud no es un número válido.")

    def validate_speed(self, value):
        # Si la velocidad viene vacía o da error en la app, la dejamos en 0.0 de forma segura
        if not value or str(value).strip() == "" or "variable" in str(value):
            return 0.0
        try:
            return float(str(value).replace(",", "."))
        except ValueError:
            return 0.0

    def validate_timestamp(self, value):
        # Limpiamos el formato de hora de la app para que Django lo entienda
        parsed_time = parse_datetime(str(value))
        if parsed_time:
            return parsed_time
        return timezone.now() # Si falla el formato, usamos la hora actual del servidor

    class Meta:
        model = GPSPoint
        fields = "__all__"