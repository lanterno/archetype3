from django.contrib import admin

from .models import Scribe, Script, Hand, HandToItemPartImages


admin.site.register(Scribe)
admin.site.register(Script)
admin.site.register(Hand)
admin.site.register(HandToItemPartImages)
