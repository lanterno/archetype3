from rest_framework.mixins import RetrieveModelMixin, ListModelMixin
from rest_framework.viewsets import GenericViewSet
from django_filters import rest_framework as filters

from .models import Scribe, Hand
from .serializers import ScribeSerializer, HandSerializer


class ScribeViewSet(GenericViewSet, RetrieveModelMixin):
    queryset = Scribe.objects.all()
    serializer_class = ScribeSerializer


class HandViewSet(GenericViewSet, ListModelMixin, RetrieveModelMixin):
    queryset = Hand.objects.all()
    serializer_class = HandSerializer
    filter_backends = [filters.DjangoFilterBackend]
    filterset_fields = ["item_part"]
