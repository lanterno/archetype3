from django.contrib import admin

from .models import (
    Catalogue,
    CatalogueNumber,
    CurrentItem,
    HistoricalItem,
    HistoricalItemDescription,
    HistoricalItemDescriptionSource,
    ImageText,
    ItemFormat,
    ItemImage,
    ItemPart,
    Repository,
)

admin.site.register(HistoricalItem)
admin.site.register(CurrentItem)
admin.site.register(ItemPart)
admin.site.register(ItemFormat)
admin.site.register(Repository)
admin.site.register(HistoricalItemDescriptionSource)
admin.site.register(HistoricalItemDescription)
admin.site.register(Catalogue)
admin.site.register(CatalogueNumber)
admin.site.register(ItemImage)
admin.site.register(ImageText)
