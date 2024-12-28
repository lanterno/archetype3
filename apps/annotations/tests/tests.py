from rest_framework.test import APITestCase


class TestGraphViewSet(APITestCase):
    def test_list_graphs(self):
        response = self.client.get("/api/v1/manuscripts/graphs/")
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.data, [])

    def test_create_graph(self):
        response = self.client.post("/api/v1/manuscripts/graphs/", data={"image": 1})
        self.assertEqual(response.status_code, 201)
        self.assertEqual(response.data["image"], 1)
