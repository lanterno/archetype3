from django.db import models


class Character(models.Model):
    class CharacterForm(models.TextChoices):
        MAJUSCULE = "Majuscule"
        MINUSCULE = "Minuscule"
        NUMERAL = "Numeral"
        PUNCTUATION = "Punctuation"
        SYMBOL = "Symbol"

    name = models.CharField(max_length=10)
    form = models.CharField(choices=CharacterForm.choices, max_length=11, null=True, blank=True)

    def __str__(self):
        return self.name


class Allograph(models.Model):
    character = models.ForeignKey(Character, on_delete=models.CASCADE)
    name = models.CharField(max_length=10)

    def __str__(self):
        return self.name


class Graph(models.Model):
    item_image = models.ForeignKey("manuscripts.ItemImage", on_delete=models.CASCADE)
    location = models.JSONField()
    allograph = models.ForeignKey(Allograph, on_delete=models.CASCADE)
    components = models.ManyToManyField("Component")


class Feature(models.Model):
    name = models.CharField(max_length=100, unique=True)


class Component(models.Model):
    name = models.CharField(max_length=100, unique=True)
    features = models.ManyToManyField(Feature)
