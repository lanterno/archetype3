from rest_framework.routers import DefaultRouter

from .views import GraphViewSet

router = DefaultRouter()
router.register("manuscripts/graphs", GraphViewSet, basename="manuscripts-graphs")

urlpatterns = router.urls
