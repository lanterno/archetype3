from django.contrib import admin

from .models import (
    ItemFormat,
    Repository,
    CurrentItem,
    HistoricalItem,
    HistoricalItemDescriptionSource,
    HistoricalItemDescription,
    ItemPart,
    Catalogue,
    CatalogueNumber,
    ItemImage,
    ImageText,
)

admin.site.register(ItemFormat)
admin.site.register(Repository)
admin.site.register(CurrentItem)
admin.site.register(HistoricalItem)
admin.site.register(HistoricalItemDescriptionSource)
admin.site.register(HistoricalItemDescription)
admin.site.register(ItemPart)
admin.site.register(Catalogue)
admin.site.register(CatalogueNumber)
admin.site.register(ItemImage)
admin.site.register(ImageText)
