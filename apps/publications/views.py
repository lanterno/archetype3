from rest_framework.mixins import ListModelMixin, RetrieveModelMixin
from rest_framework.viewsets import GenericViewSet

from .models import Event, Publication
from .serializers import EventDetailSerializer, EventListSerializer, PublicationDetailSerializer, PublicationListSerializer


class EventViewSet(GenericViewSet, ListModelMixin, RetrieveModelMixin):
    queryset = Event.objects.all()
    serializer_class = EventDetailSerializer

    def get_serializer_class(self):
        if self.action == "list":
            return EventListSerializer
        return EventDetailSerializer


class PublicationViewSet(GenericViewSet, ListModelMixin, RetrieveModelMixin):
    queryset = Publication.objects.all()
    serializer_class = PublicationDetailSerializer

    def get_serializer_class(self):
        if self.action == "list":
            return PublicationListSerializer
        return PublicationDetailSerializer

    def get_queryset(self):
        return Publication.objects.filter(status=Publication.Status.PUBLISHED)
