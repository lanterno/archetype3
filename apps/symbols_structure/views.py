from rest_framework.generics import ListAPIView

from .models import Allograph
from .serializers import AllographSerializer


class AllographListView(ListAPIView):
    queryset = Allograph.objects.all()
    serializer_class = AllographSerializer
    pagination_class = None
