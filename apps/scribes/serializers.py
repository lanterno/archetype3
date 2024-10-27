from rest_framework import serializers

from .models import Scribe


class ScribeSerializer(serializers.ModelSerializer):

    class Meta:
        model = Scribe
        fields = ["id", "name", "period", "scriptorium"]
