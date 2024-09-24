from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import include, path
from rest_framework import routers

from apps.common.views import APISchemaView, SwaggerUIView

router = routers.SimpleRouter(trailing_slash=False)

urlpatterns = (
    [
        path("api/v1/", include(router.urls)),
        path("api/v1/auth/", include("apps.users.urls")),
        path("api/v1/media/", include("apps.publications.urls")),
        path("admin/", admin.site.urls),
        path("api/v1/schema/", APISchemaView.as_view(), name="doc-schema"),
        path("api/v1/docs/", SwaggerUIView.as_view(), name="doc-ui"),
        path("tinymce/", include("tinymce.urls")),
    ]
    + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
)
