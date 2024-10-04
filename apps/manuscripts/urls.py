from rest_framework.routers import DefaultRouter

from .views import ItemPartViewSet

router = DefaultRouter()
router.register("item-parts", ItemPartViewSet)

urlpatterns = router.urls
