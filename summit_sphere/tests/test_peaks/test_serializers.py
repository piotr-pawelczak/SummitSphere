import pytest

from summit_sphere.peaks.serializers import (
    PeakDetailsSerializer,
    PeakListSerializer,
    RegionSerializer,
)


class TestRegionSerializer:
    @pytest.mark.unit
    def test_returns_valid_data(self, region):
        # Arrange
        expected_data = {"pk": region.pk, "name": region.name}

        # Act
        serializer = RegionSerializer(region)

        # Assert
        assert expected_data == serializer.data


class TestPeakListSerializer:
    @pytest.mark.unit
    def test_returns_valid_data(self, peak):
        # Arrange
        expected_data = {
            "pk": peak.pk,
            "name": peak.name,
            "elevation": float(peak.elevation),
            "region": peak.region.name,
            "country_code": peak.country_code,
        }

        # Act
        serializer = PeakListSerializer(peak)

        # Assert
        assert expected_data == serializer.data


class TestPeakDetailsSerializer:
    @pytest.mark.unit
    def test_returns_valid_data(self, peak):
        # Arrange
        expected_data = {
            "pk": peak.pk,
            "name": peak.name,
            "elevation": float(peak.elevation),
            "region": RegionSerializer(peak.region).data,
            "country_code": peak.country_code,
            "alternative_names": peak.alternative_names,
            "latitude": float(peak.latitude),
            "longitude": float(peak.longitude),
        }

        # Act
        serializer = PeakDetailsSerializer(peak)

        # Assert
        assert expected_data == serializer.data
