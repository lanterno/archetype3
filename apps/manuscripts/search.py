from drf_haystack.serializers import HaystackSerializer, HaystackFacetSerializer
from drf_haystack.viewsets import HaystackViewSet
from drf_haystack.mixins import FacetMixin

from .search_indexes import ItemPartIndex
from .models import ItemPart


class ManuscriptSearchSerializer(HaystackSerializer):
    class Meta:
        index_classes = [ItemPartIndex]

        fields = [
            "repository_city",
            "repository_name",
            "shelfmark",
            "catalogue_numbers",
            "date",
            "type",
            "number_of_images",
            "issuer_name",
            "named_beneficiary",
        ]


class ManuscriptFacetSearchSerializer(HaystackFacetSerializer):

    serialize_objects = True

    class Meta(ManuscriptSearchSerializer.Meta):
        field_options = {
            "number_of_images": {},
            "type": {},
            "repository_city": {},
            "repository_name": {},
            "named_beneficiary": {},
            "issuer_name": {},
        }


class ManuscriptSearchViewSet(FacetMixin, HaystackViewSet):
    index_models = [ItemPart]
    serializer_class = ManuscriptSearchSerializer
    facet_serializer_class = ManuscriptFacetSearchSerializer
