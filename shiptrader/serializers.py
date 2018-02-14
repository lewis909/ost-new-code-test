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

    def create(self, validated_data):
        return Starship.objects.create(**validated_data)


class ListingsSerializer(serializers.ModelSerializer):

    id = serializers.IntegerField(read_only=True)
    name = serializers.CharField(max_length=255)
    ship_type = StarshipSerializer()
    price = serializers.IntegerField()
    active = serializers.BooleanField()

    class Meta:
        model = Listing
        fields = (
            'id',
            'name',
            'ship_type',
            'price',
            'active'
        )

    def create(self, validated_data):
        starship_data = validated_data.pop('ship_type', None)
        if starship_data:
            ship = Starship.objects.get(starship_class=starship_data['starship_class'])
            validated_data['ship_type'] = ship

            return Listing.objects.create(**validated_data)

