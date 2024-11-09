import nested_admin

from django.contrib import admin

from .models import Allograph, AllographComponent, Aspect, Character, Component, Feature, Graph


@admin.register(Character)
class CharacterAdmin(admin.ModelAdmin):
    list_display = ("name", "type")


class AllographComponentFeatureInline(nested_admin.NestedStackedInline):
    model = AllographComponent.features.through
    extra = 1
    fields = ["allograph_component", "feature", "set_by_default"]


class AllographComponentInline(nested_admin.NestedTabularInline):
    model = AllographComponent
    inlines = [AllographComponentFeatureInline]
    extra = 1
    fields = ["component"]


@admin.register(Allograph)
class AllographAdmin(nested_admin.NestedModelAdmin):
    list_display = ["name", "character"]
    filter_horizontal = ["aspects"]
    inlines = [AllographComponentInline]

    fieldsets = (
        (None, {"fields": ("name", "character")}),
        ("Aspects", {"fields": ("aspects",)}),
    )


admin.site.register(Graph)
admin.site.register(Feature)
admin.site.register(Component)
admin.site.register(Aspect)
