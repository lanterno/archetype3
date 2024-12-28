from rest_framework import viewsets

from .models import Graph
from .serializers import GraphSerializer


class GraphViewSet(viewsets.ModelViewSet):
    queryset = Graph.objects.all()
    serializer_class = GraphSerializer
    pagination_class = None
    filterset_fields = ["item_image"]
