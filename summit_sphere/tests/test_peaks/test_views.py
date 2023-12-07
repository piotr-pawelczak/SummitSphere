import pytest

from summit_sphere.peaks.serializers import PeakDetailsSerializer, PeakListSerializer
from summit_sphere.tests.test_peaks.factories import PeakFactory

pytestmark = pytest.mark.django_db


class TestPeakViewSet:
    endpoint = "/api/peaks/"

    @pytest.mark.parametrize("batch_size", [3, 5])
    def test_list(self, api_client, batch_size):
        # Arrange
        peaks = PeakFactory.create_batch(batch_size)
        serializer = PeakListSerializer(peaks, many=True)

        # Act
        response = api_client.get(self.endpoint)
        response_data = response.json()

        # Assert
        assert response.status_code == 200
        assert response_data["count"] == batch_size
        assert response_data["results"] == serializer.data
        assert "next" in response_data.keys()
        assert "previous" in response_data.keys()

    @pytest.mark.parametrize("batch_size", [3, 5, 10])
    def test_list_num_of_queries(self, api_client, capture_queries, batch_size):
        # Arrange
        PeakFactory.create_batch(batch_size)

        # Act
        with capture_queries:
            response = api_client.get(self.endpoint)

        # Assert
        assert response.status_code == 200
        assert len(capture_queries) == 2

    def test_retrieve(self, api_client):
        # Arrange
        peak = PeakFactory()
        url = f"{self.endpoint}{peak.pk}/"
        serializer = PeakDetailsSerializer(peak)

        # Act
        response = api_client.get(url)

        # Assert
        assert response.status_code == 200
        assert response.json() == serializer.data

    def test_retrieve_num_queries(self, api_client, capture_queries):
        # Arrange
        peak = PeakFactory()
        url = f"{self.endpoint}{peak.pk}/"

        # Act
        with capture_queries:
            response = api_client.get(url)
        captured_queries = len(capture_queries)

        assert response.status_code == 200
        assert captured_queries == 1
