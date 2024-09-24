from django.contrib import admin

from .models import Hand, HandToItemPartImages, Scribe, Script

admin.site.register(Scribe)
admin.site.register(Script)
admin.site.register(Hand)
admin.site.register(HandToItemPartImages)
