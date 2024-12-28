from rest_framework import serializers

from .models import Graph


class GraphComponentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Graph.components.through
        fields = ["component", "features"]


class GraphSerializer(serializers.ModelSerializer):
    components = GraphComponentSerializer(many=True)

    class Meta:
        model = Graph
        fields = ["id", "item_image_id", "annotation", "allograph_id", "components", "hand_id"]

    def create(self, validated_data):
        components_data = validated_data.pop("components")
        graph = Graph.objects.create(**validated_data)
        # use the GraphComponentSerializer to create the components and features
        for component_data in components_data:
            features_data = component_data.pop("features")
            component = Graph.components.through.objects.create(graph=graph, **component_data)
            component.features.set(features_data)
        return graph
