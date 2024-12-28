import factory

from apps.symbols_structure.models import Allograph, Character


class CharacterFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Character

    name = factory.Faker("random_lowercase_letter")
    type = Character.CharacterForm.MINUSCULE_LETTER


class AllographFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Allograph

    character = factory.SubFactory(CharacterFactory)
    name = factory.Faker("random_lowercase_letter")