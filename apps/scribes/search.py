from drf_haystack.serializers import HaystackSerializer
from drf_haystack.viewsets import HaystackViewSet

from .search_indexes import ScribeIndex
from .models import Scribe


class ScribeSearchSerializer(HaystackSerializer):
    class Meta:
        index_classes = [ScribeIndex]

        fields = ["name", "period", "scriptorium"]


class ScribeSearchViewSet(HaystackViewSet):
    index_models = [Scribe]
    serializer_class = ScribeSearchSerializer
