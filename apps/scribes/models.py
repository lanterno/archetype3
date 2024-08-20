from django.db import models


class Scribe(models.Model):
    name = models.CharField(max_length=100)
    period = models.CharField(max_length=100)
    scriptorium = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Script(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Hand(models.Model):
    scribe = models.ForeignKey(Scribe, on_delete=models.PROTECT)
    script = models.ForeignKey(Script, on_delete=models.PROTECT)

    name = models.CharField(max_length=100)
    item_part = models.ForeignKey("manuscripts.ItemPart", on_delete=models.PROTECT)
    date = models.CharField(max_length=100)
    place = models.CharField(max_length=100)

    description = models.TextField()
    item_part_images = models.ManyToManyField(
        "manuscripts.ItemPart",
        through="HandToItemPartImages",
        related_name="hands",
    )

    def __str__(self):
        return self.name


class HandToItemPartImages(models.Model):
    hand = models.ForeignKey(Hand, on_delete=models.PROTECT)
    item_part = models.ForeignKey("manuscripts.ItemPart", on_delete=models.PROTECT)
