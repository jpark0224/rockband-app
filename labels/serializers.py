from labels.models import Label
from rest_framework import serializers


class LabelSerializer(serializers.ModelSerializer):
    managed_bands = serializers.StringRelatedField(read_only=True, many=True)

    class Meta:
        model = Label
        fields = ("name", "founded_year", "managed_bands")
