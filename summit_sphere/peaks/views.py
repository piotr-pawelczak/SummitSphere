from rest_framework import viewsets

from .models import Peak
from .serializers import PeakDetailsSerializer, PeakListSerializer


class PeakViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Peak.objects.all()
    serializer_class = PeakListSerializer

    def get_queryset(self):
        return self.queryset.select_related("region")

    def get_serializer_class(self):
        if self.action == "retrieve":
            return PeakDetailsSerializer
        return self.serializer_class
