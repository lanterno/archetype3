from drf_haystack.serializers import HaystackSerializer
from drf_haystack.viewsets import HaystackViewSet

from .search_indexes import ItemPartIndex
from .models import ItemPart


class ManuscriptSearchSerializer(HaystackSerializer):
    class Meta:
        index_classes = [ItemPartIndex]

        fields = ["repository_name", "repository_city", "shelfmark", "current_item"]


class ManuscriptSearchViewSet(HaystackViewSet):
    index_models = [ItemPart]
    serializer_class = ManuscriptSearchSerializer
