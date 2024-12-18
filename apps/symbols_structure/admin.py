import nested_admin
from django.contrib import admin

from apps.symbols_structure.models import Allograph, AllographComponent, Aspect, Character, Component, Feature


@admin.register(Character)
class CharacterAdmin(admin.ModelAdmin):
    list_display = ("name", "type")


class AllographComponentFeatureInline(nested_admin.nested.NestedStackedInline):
    model = AllographComponent.features.through
    extra = 1
    fields = ["allograph_component", "feature", "set_by_default"]


class AllographComponentInline(nested_admin.nested.NestedTabularInline):
    model = AllographComponent
    inlines = [AllographComponentFeatureInline]
    extra = 1
    fields = ["component"]


@admin.register(Allograph)
class AllographAdmin(nested_admin.nested.NestedModelAdmin):
    list_display = ["name", "character"]
    filter_horizontal = ["aspects"]
    inlines = [AllographComponentInline]

    fieldsets = (
        (None, {"fields": ("name", "character")}),
        ("Aspects", {"fields": ("aspects",)}),
    )


@admin.register(Component)
class ComponentAdmin(admin.ModelAdmin):
    list_display = ["name"]
    fields = ["name", "features"]
    filter_horizontal = ["features"]


admin.site.register(Feature)
admin.site.register(Aspect)
