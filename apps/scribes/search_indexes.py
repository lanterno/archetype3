from haystack import indexes
from apps.scribes.models import Scribe


class ScribeIndex(indexes.SearchIndex, indexes.Indexable):
    text = indexes.CharField(document=True, use_template=False)
    name = indexes.CharField(model_attr="name")
    period = indexes.CharField(model_attr="period")
    scriptorium = indexes.CharField(model_attr="scriptorium")

    def get_model(self):
        return Scribe
