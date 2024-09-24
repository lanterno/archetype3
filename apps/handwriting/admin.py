from django.contrib import admin

from .models import Allograph, Character, Component, Feature, Graph

admin.site.register(Character)
admin.site.register(Allograph)
admin.site.register(Graph)
admin.site.register(Feature)
admin.site.register(Component)
