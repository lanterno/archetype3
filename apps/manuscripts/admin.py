from django.contrib import admin

from .models import (
    CatalogueNumber,
    CurrentItem,
    HistoricalItem,
    HistoricalItemDescription,
    ImageText,
    ItemFormat,
    ItemImage,
    ItemPart,
    Repository,
)


class HistoricalItemAdmin(admin.ModelAdmin):
    list_display = ["id", "date", "issuer", "named_beneficiary"]
    search_fields = ["date", "issuer", "named_beneficiary"]


class CurrentItemAdmin(admin.ModelAdmin):
    list_display = ["id", "repository", "shelfmark", "number_of_parts"]
    search_fields = ["repository__name", "shelfmark"]
    list_filter = ["repository"]


class RepositoryAdmin(admin.ModelAdmin):
    list_display = ["name", "label", "place", "url"]
    search_fields = ["name", "label"]


admin.site.register(HistoricalItem, HistoricalItemAdmin)
admin.site.register(CurrentItem, CurrentItemAdmin)
admin.site.register(ItemPart)
admin.site.register(ItemFormat)
admin.site.register(Repository, RepositoryAdmin)
admin.site.register(HistoricalItemDescription)
admin.site.register(CatalogueNumber)
admin.site.register(ItemImage)
admin.site.register(ImageText)
