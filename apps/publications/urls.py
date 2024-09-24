from rest_framework import routers

from .views import EventViewSet, PublicationViewSet

router = routers.DefaultRouter()

router.register(r"events", EventViewSet, basename="events")
router.register(r"publications", PublicationViewSet, basename="publications")

urlpatterns = router.urls
