from django.urls import path

from .views import AllographListView

urlpatterns = [
    path("allographs/", AllographListView.as_view(), name="allograph-list"),
]
