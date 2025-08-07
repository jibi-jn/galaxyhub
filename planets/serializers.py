from rest_framework import serializers
from .models import Planet

class PlanetSerializer(serializers.ModelSerializer):
    """
    Serializer for the Planet model.
    """
    class Meta:
        model = Planet
        fields = '__all__'
