from rest_framework import viewsets
from .models import Planet
from .serializers import PlanetSerializer

class PlanetModelViewSet(viewsets.ModelViewSet):
    """
    A viewset that provides the standard actions (list, create, retrieve, update, destroy)
    for the Planet model.
    """
    queryset = Planet.objects.all()
    serializer_class = PlanetSerializer
