from rest_framework.routers import DefaultRouter

from .views import ScribeViewSet, HandViewSet

router = DefaultRouter()
router.register("scribes", ScribeViewSet)
router.register("hands", HandViewSet)


urlpatterns = router.urls
