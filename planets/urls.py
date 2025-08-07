from rest_framework.routers import DefaultRouter
from .views import PlanetModelViewSet

router = DefaultRouter()
router.register(r'planets', PlanetModelViewSet, basename='planet')

urlpatterns = router.urls
