from django.contrib import admin

from .models import Hand, HandToItemPartImages, Scribe, Script


class ScribeAdmin(admin.ModelAdmin):
    list_display = ["name", "period", "scriptorium"]
    search_fields = ["name", "period", "scriptorium"]


class HandAdmin(admin.ModelAdmin):
    list_display = ["id", "item_part", "name", "scribe", "script", "date", "place"]


admin.site.register(Scribe, ScribeAdmin)
admin.site.register(Script)
admin.site.register(Hand, HandAdmin)
admin.site.register(HandToItemPartImages)
