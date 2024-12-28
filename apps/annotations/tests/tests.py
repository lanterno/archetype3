import rest_framework
from rest_framework.test import APITestCase

from apps.annotations.tests.factories import GraphFactory
from apps.manuscripts.tests.factories import ItemImageFactory
from apps.scribes.tests.factories import HandFactory
from apps.symbols_structure.tests.tests import AllographFactory
from apps.users.tests.factories import AdminFactory


# question: is there a key binding shortcut in VSCode
# to import a highlighted class?
# answer: yes, ctrl + . (period)
class TestGraphViewSet(APITestCase):

    def setUp(self):
        admin = AdminFactory()
        self.client.force_authenticate(user=admin)
        self.item_image = ItemImageFactory()
        self.item_part = self.item_image.item_part
        self.allograph = AllographFactory()
        self.hand = HandFactory(item_part=self.item_part)

        self.graphs = GraphFactory.create_batch(3, item_image=self.item_image, allograph=self.allograph, hand=self.hand)

    def test_list_graphs(self):
        response = self.client.get("/api/v1/manuscripts/graphs/")
        assert response.status_code == rest_framework.status.HTTP_200_OK, response.data
        assert len(response.data) == 3, response.data

    def test_create_graph(self):
        response = self.client.post(
            "/api/v1/manuscripts/graphs/",
            data={
                "item_image": self.item_image.id,
                "annotation": {"x": 0, "y": 0, "width": 100, "height": 100},
                "allograph": self.allograph.id,
                "hand": self.hand.id,
                "components": [],
            },
            format="json",
        )
        assert response.status_code == rest_framework.status.HTTP_201_CREATED, response.data
