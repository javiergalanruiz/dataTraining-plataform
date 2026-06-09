import re
from rest_framework import serializers
from .models import GPSPoint
from django.utils.dateparse import parse_datetime
from django.utils import timezone


def clean_coord(value):
    if value is None:
        raise ValueError()

    value = str(value).strip()

    match = re.search(r"-?\d+(\.\d+)?", value.replace(",", "."))
    if not match:
        raise ValueError()

    return float(match.group())


class GPSPointSerializer(serializers.ModelSerializer):

    lat = serializers.CharField()
    lon = serializers.CharField()
    speed = serializers.CharField(required=False, allow_blank=True, allow_null=True)
    timestamp = serializers.CharField()

    def validate_lat(self, value):
        try:
            return clean_coord(value)
        except ValueError:
            raise serializers.ValidationError("Latitud no es válida")

    def validate_lon(self, value):
        try:
            return clean_coord(value)
        except ValueError:
            raise serializers.ValidationError("Longitud no es válida")

    def validate_speed(self, value):
        if not value or "variable" in str(value):
            return 0.0
        try:
            return float(str(value).replace(",", "."))
        except ValueError:
            return 0.0

    def validate_timestamp(self, value):
        parsed_time = parse_datetime(str(value))
        return parsed_time or timezone.now()

    class Meta:
        model = GPSPoint
        fields = "__all__"