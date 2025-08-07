from django.db import models
    
class Planet(models.Model):
    """
    A model representing a planet in the system.
    """
    name = models.CharField(max_length=100, unique=True)
    population = models.BigIntegerField(null=True, blank=True)
    terrains = models.JSONField(null=True, blank=True)
    climates = models.JSONField(null=True, blank=True)

    def __str__(self):
        return self.name
