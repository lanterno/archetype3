from django.db import models


class ItemFormat(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Repository(models.Model):
    class Type(models.TextChoices):
        LIBRARY = "Library"
        INSTITUTION = "Institution"
        PERSON = "Person"
        ONLINE_RESOURCE = "Online Resource"

    name = models.CharField(max_length=100)
    label = models.CharField(max_length=30)
    place = models.CharField(max_length=50)
    url = models.URLField(null=True)
    type = models.CharField(max_length=30, choices=Type.choices, null=True)

    def __str__(self):
        return self.label

    class Meta:
        verbose_name_plural = "Repositories"


class CurrentItem(models.Model):
    description = models.TextField(blank=True)
    repository = models.ForeignKey(Repository, on_delete=models.CASCADE)
    shelfmark = models.CharField(max_length=60)

    def __str__(self):
        return f"{self.repository.label} {self.shelfmark}"

    def number_of_parts(self):
        return self.itempart_set.count()


class HistoricalItem(models.Model):
    class Type(models.TextChoices):
        AGREEMENT = "Agreement"
        CHARTER = "Charter"
        LETTER = "Letter"

    class HairType(models.TextChoices):
        FHFH = "FHFH", "FHFH"
        FHHF = "FHHF", "FHHF"
        HFFH = "HFFH", "HFFH"
        HFHF = "HFHF", "HFHF"
        MIXED = "Mixed", "Mixed"

    type = models.CharField(max_length=20, choices=Type.choices)
    format = models.ForeignKey(ItemFormat, null=True, on_delete=models.SET_NULL)
    language = models.CharField(max_length=100)

    vernacular = models.BooleanField(null=True)
    neumed = models.BooleanField(null=True)
    hair_type = models.CharField(max_length=20, choices=HairType.choices, null=True)

    date = models.CharField(max_length=100)
    date_sort = models.CharField(max_length=100)

    issuer = models.CharField(max_length=100)
    named_beneficiary = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.get_type_display()} - {self.id}"


class HistoricalItemDescription(models.Model):
    historical_item = models.ForeignKey(HistoricalItem, related_name="descriptions", on_delete=models.CASCADE)
    source = models.ForeignKey(Repository, on_delete=models.CASCADE)
    content = models.TextField()


class ItemPart(models.Model):
    historical_item = models.ForeignKey(HistoricalItem, on_delete=models.CASCADE)
    current_item = models.ForeignKey(CurrentItem, on_delete=models.CASCADE)


class CatalogueNumber(models.Model):
    historical_item = models.ForeignKey(HistoricalItem, related_name="catalogue_numbers", on_delete=models.CASCADE)
    number = models.CharField(max_length=30)
    catalogue = models.ForeignKey(Repository, on_delete=models.CASCADE)
    url = models.URLField(null=True)

    def __str__(self):
        return f"{self.catalogue.label} {self.number}"


class ItemImage(models.Model):
    item_part = models.ForeignKey(ItemPart, on_delete=models.CASCADE)
    image = models.ImageField(upload_to="historical_items")
    locus = models.CharField(max_length=20, null=True)
    folio_side = models.CharField(max_length=20, null=True)
    folio_number = models.CharField(max_length=20, null=True)

    def number_of_annotations(self):
        return self.graphs.count()


class ImageText(models.Model):
    class Type(models.TextChoices):
        TRANSCRIPTION = "Transcription"
        TRANSLATION = "Translation"

    class Status(models.TextChoices):
        DRAFT = "Draft"
        REVIEW = "Review"
        LIVE = "Live"

    item_image = models.ForeignKey(ItemImage, related_name="texts", on_delete=models.CASCADE)
    content = models.TextField()
    type = models.CharField(max_length=13, choices=Type.choices)
    status = models.CharField(max_length=6, choices=Status.choices)
