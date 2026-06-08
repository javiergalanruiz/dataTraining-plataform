from django.urls import path
from .views import GPSIngestView, map_view, obtener_puntos

urlpatterns = [
    path("ingest/", GPSIngestView.as_view()),
    path("", map_view),
    path("points/", obtener_puntos, name='obtener_puntos'),
]