from django.contrib import admin
from django.urls import path

urlpatterns = [
    path('admin/', admin.site.urls),
    path("api/v1/schema/", APISchemaView.as_view(), name="doc-schema"),
    path("api/v1/docs/", SwaggerUIView.as_view(), name="doc-ui"),
]
