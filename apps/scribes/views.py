from rest_framework.viewsets import GenericViewSet
from rest_framework.mixins import RetrieveModelMixin

from .models import Scribe
from .serializers import ScribeSerializer


class ScribeViewSet(GenericViewSet, RetrieveModelMixin):
    queryset = Scribe.objects.all()
    serializer_class = ScribeSerializer
