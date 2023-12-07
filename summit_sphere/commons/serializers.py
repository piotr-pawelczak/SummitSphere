from typing import OrderedDict

from rest_framework import serializers


class ReadOnlyModelSerializer(serializers.ModelSerializer):
    def get_fields(self) -> OrderedDict[str, serializers.Field]:
        """
        Get the fields for the serializer and set them to read-only.

        Returns:
            OrderedDict: The fields for the serializer.
        """
        fields = super().get_fields()
        for field_value in fields.values():
            field_value.read_only = True
        return fields
