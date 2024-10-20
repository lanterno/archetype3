from django.contrib import admin

from .models import Hand, HandToItemPartImages, Scribe, Script


class ScribeAdmin(admin.ModelAdmin):
    list_display = ["name", "period", "scriptorium"]
    search_fields = ["name", "period", "scriptorium"]


admin.site.register(Scribe, ScribeAdmin)
admin.site.register(Script)
admin.site.register(Hand)
admin.site.register(HandToItemPartImages)
