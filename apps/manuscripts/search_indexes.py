from haystack import indexes
from apps.manuscripts.models import ItemPart


class ItemPartIndex(indexes.ModelSearchIndex, indexes.Indexable):
    text = indexes.CharField(document=True, use_template=False)
    repository_name = indexes.CharField(model_attr="current_item__repository__name")
    repository_city = indexes.CharField(model_attr="current_item__repository__place")
    shelfmark = indexes.CharField(model_attr="current_item__shelfmark")
    current_item = indexes.CharField(model_attr="current_item")

    # 	repository_city, repository_name, Shelfmark, category_number, date,
    #   type, number_of_parts, issuer_name, named_beneficiary

    # Facets:
    # Image availability: With_images, Without_images
    # Type: Charter, Letter, Agreement..
    # repository_city, repostory
    # issuer_type, issuer
    # named_beneficiary
    class Meta:
        model = ItemPart
        fields = ["text", "repository_name", "repository_city", "shelfmark", "current_item"]

    def get_model(self):
        return ItemPart
