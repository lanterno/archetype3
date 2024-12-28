from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import include, path
from rest_framework import routers

from apps.common.views import APISchemaView, SwaggerUIView
from apps.manuscripts.search import ManuscriptSearchViewSet
from apps.scribes.search import ScribeSearchViewSet

search_router = routers.DefaultRouter(trailing_slash=False)
search_router.register("item-parts", ManuscriptSearchViewSet, basename="item-parts")
search_router.register("scribes", ScribeSearchViewSet, basename="scribes")


urlpatterns = (
    [
        path("tinymce/", include("tinymce.urls")),
        path("admin/", admin.site.urls),
        path("api/v1/search/", include(search_router.urls)),
        path("api/v1/auth/", include("apps.users.urls")),
        path("api/v1/media/", include("apps.publications.urls")),
        path("api/v1/manuscripts/", include("apps.manuscripts.urls")),
        path("api/v1/", include("apps.annotations.urls")),
        path("api/v1/", include("apps.scribes.urls")),
        # path("api/v1/symbols_structure/", include("apps.symbols_structure.urls")),
        path("api/v1/schema/", APISchemaView.as_view(), name="doc-schema"),
        path("api/v1/docs/", SwaggerUIView.as_view(), name="doc-ui"),
    ]
    + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
)
