import requests
from django.core.management.base import BaseCommand
from planets.models import Planet

class Command(BaseCommand):
    help = 'Fetch planets from SWAPI GraphQL and store in DB'

    def handle(self, *args, **kwargs):
        """
        Fetches planet data from the SWAPI GraphQL API and saves it to the database.
        Updates existing planets based on the name field.
        """

        url = "https://swapi-graphql.netlify.app/.netlify/functions/index"
        query = "query Query { allPlanets { planets { name population terrains climates } } }"

        response = requests.get(url, params={'query': query})
        data = response.json()
        response.raise_for_status()

        planets = data.get("data", {}).get("allPlanets", {}).get("planets", [])

        planet_objs = []
        for planet_data in planets:
            planet_objs.append(Planet(
                name=planet_data["name"],
                population=planet_data.get("population"),
                terrains=planet_data.get("terrains", []),
                climates=planet_data.get("climates", []),
            ))

        Planet.objects.bulk_create(
            planet_objs,
            update_conflicts=True,
            update_fields=["population", "terrains", "climates"],
            unique_fields=["name"]
        )

        self.stdout.write(f"Bulk saved {len(planet_objs)} planets.")
