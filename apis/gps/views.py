

# Create your views here.
from rest_framework.views import APIView
from django.http import JsonResponse
from rest_framework.response import Response
from .models import GPSPoint
from .serializers import GPSPointSerializer
from django.shortcuts import render
from .models import GPSPoint

class GPSIngestView(APIView):

     def post(self, request):

        serializer = GPSPointSerializer(data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response({"status": "ok"})

        return Response(serializer.errors, status=400)


def map_view(request):
    return render(request, "inicio.html")


def gps_points(request):

    points = GPSPoint.objects.all().values(
        "lat",
        "lon",
        "speed",
        "timestamp"
    )

    return JsonResponse(list(points), safe=False)


