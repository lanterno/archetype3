from django_filters import rest_framework as filters
from rest_framework.mixins import ListModelMixin, RetrieveModelMixin
from rest_framework.viewsets import GenericViewSet

from .models import Hand, Scribe
from .serializers import HandSerializer, ScribeSerializer


class ScribeViewSet(GenericViewSet, RetrieveModelMixin):
    queryset = Scribe.objects.all()
    serializer_class = ScribeSerializer


class HandViewSet(GenericViewSet, ListModelMixin, RetrieveModelMixin):
    queryset = Hand.objects.all()
    serializer_class = HandSerializer
    filter_backends = [filters.DjangoFilterBackend]
    filterset_fields = ["item_part"]
