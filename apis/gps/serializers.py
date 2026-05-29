from rest_framework import serializers
from .models import GPSPoint

class GPSPointSerializer(serializers.ModelSerializer):

    def validate_lat(self, value):
        return float(str(value).replace(",", "."))

    def validate_lon(self, value):
        return float(str(value).replace(",", "."))

    class Meta:
        model = GPSPoint
        fields = "__all__"