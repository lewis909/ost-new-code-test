from rest_framework import serializers
from shiptrader.models import Listing, Starship


class StarshipSerializer(serializers.ModelSerializer):

    id = serializers.IntegerField(read_only=True)
    starship_class = serializers.CharField(max_length=255)
    manufacturer = serializers.CharField(max_length=255)
    length = serializers.FloatField()
    hyperdrive_rating = serializers.FloatField()
    cargo_capacity = serializers.IntegerField()
    crew = serializers.IntegerField()
    passengers = serializers.IntegerField()

    class Meta:
        model = Starship

        fields = (
            'id',
            'starship_class',
            'manufacturer',
            'length',
            'hyperdrive_rating',
            'cargo_capacity',
            'crew',
            'passengers'

        )


class listingsSerializer(serializers.ModelSerializer):

    id = serializers.IntegerField(read_only=True)
    name = serializers.CharField(max_length=255)
    ship_type = serializers.PrimaryKeyRelatedField(queryset=Starship.objects.all())
    price = serializers.IntegerField()

    class Meta:
        model = Listing
        fields = (
            'id',
            'name',
            'ship_type',
            'price'
        )
