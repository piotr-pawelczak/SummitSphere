from rest_framework import serializers

from summit_sphere.commons.serializers import ReadOnlyModelSerializer

from .models import Peak, Region


class RegionSerializer(ReadOnlyModelSerializer):
    class Meta:
        model = Region
        fields = ["pk", "name"]


class PeakBaseSerializer(ReadOnlyModelSerializer):
    elevation = serializers.FloatField()

    class Meta:
        model = Peak
        fields = ["pk", "name", "elevation", "region", "country_code"]


class PeakListSerializer(PeakBaseSerializer):
    region = serializers.StringRelatedField()


class PeakDetailsSerializer(PeakBaseSerializer):
    region = RegionSerializer()

    class Meta:
        model = Peak
        fields = PeakBaseSerializer.Meta.fields + [
            "alternative_names",
            "latitude",
            "longitude",
        ]
