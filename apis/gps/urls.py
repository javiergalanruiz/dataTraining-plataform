from django.urls import path
from .views import GPSIngestView, map_view, gps_points

urlpatterns = [
    path("ingest/", GPSIngestView.as_view()),
    path("", map_view),
    path("points/", gps_points),
    
]