from cProfile import label
from rest_framework import serializers

from labels.models import Label
from .models import Album, Band


class LabelSerializer(serializers.ModelSerializer):
    class Meta:
        model = Label
        fields = ("name", "founded_year")


class AlbumSerializer(serializers.ModelSerializer):
    class Meta:
        model = Album
        fields = ("band")


class BandSerializer(serializers.ModelSerializer):
    label = LabelSerializer()

    leader = serializers.StringRelatedField()
    members = serializers.StringRelatedField(
        many=True, read_only=True)

    class Meta:
        model = Band
        fields = '__all__'

    # to serialize the creation of the nested resources
    def create(self, data):
        # remove label data in a band data
        label_data = data.pop("label")
        band = Band(**data)
        label, _created = Label.objects.get_or_create(**label_data)

        band.label = label
        band.save()

        # data doesn't have label_data from this point
        return band

    def update(self, band, data):
        label_data = data.pop("label")

        band.name = data.get("name", band.name)
        band.genres = data.get("genres", band.genres)
        band.origin = data.get("origin", band.origin)
        band.year_formed = data.get("year_formed", band.year_formed)
        band.active = data.get("active", band.active)

        if label_data:
            label, _created = Label.objects.get_or_create(**label_data)
            band.label = label

        band.save()

        # data doesn't have label_data from this point
        return band
