from rest_framework.routers import DefaultRouter

from .views import ScribeViewSet

router = DefaultRouter()
router.register("scribes", ScribeViewSet)

urlpatterns = router.urls
