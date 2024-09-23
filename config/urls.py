from django.contrib import admin
from django.urls import include, path
from rest_framework import routers

from apps.common.views import APISchemaView, SwaggerUIView

router = routers.SimpleRouter(trailing_slash=False)

urlpatterns = [
    path("api/v1/", include(router.urls)),
    path("api/v1/auth", include("apps.users.urls")),
    path("admin/", admin.site.urls),
    path("api/v1/schema/", APISchemaView.as_view(), name="doc-schema"),
    path("api/v1/docs/", SwaggerUIView.as_view(), name="doc-ui"),
]
