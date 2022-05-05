from rest_framework import serializers
from api import models
from api import services


class CrewSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Crew
        fields = ['id', 'name', 'ship']

    def get_validation_exclusions(self):
        exclusions = super(CrewSerializer, self).get_validation_exclusions()
        return exclusions + ['id', 'created_at,', 'updated_at']

    def create(self, validated_data):
        return services.create_crew(validated_data['ship'], name=validated_data['name'])


class ShipSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Ship
        fields = ('id', 'mother_ship')

    def get_validation_exclusions(self):
        exclusions = super(ShipSerializer, self).get_validation_exclusions()
        return exclusions + ['id', 'created_at,', 'updated_at']

    def create(self, validated_data):
        return services.create_ship(validated_data['mother_ship'])


class CrewDetailsSerializer(serializers.ModelSerializer):
    ship = ShipSerializer()

    class Meta:
        model = models.Crew
        fields = ['id', 'name', 'created_at', 'updated_at', 'ship']

    def get_validation_exclusions(self):
        exclusions = super(CrewDetailsSerializer, self).get_validation_exclusions()
        return exclusions + ['id', 'created_at,', 'updated_at']



class MotherShipSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.MotherShip
        fields = ['id']

    def get_validation_exclusions(self):
        exclusions = super(MotherShipSerializer, self).get_validation_exclusions()
        return exclusions + ['id', 'created_at,', 'updated_at']

    def create(self, validated_data):
        return services.create_mother_ship()


class ShipDetailsSerializer(serializers.ModelSerializer):
    crew = CrewSerializer(source='crew_set', many=True)
    mother_ship = MotherShipSerializer()

    class Meta:
        model = models.Ship
        fields = ('id', 'created_at', 'mother_ship', 'crew')

    def get_validation_exclusions(self):
        exclusions = super(ShipDetailsSerializer, self).get_validation_exclusions()
        return exclusions + ['id', 'created_at,', 'updated_at']


class MotherShipDetailsSerializer(serializers.ModelSerializer):
    ships = ShipSerializer(source='ship_set', many=True)

    class Meta:
        model = models.MotherShip
        fields = ['id', 'created_at', 'updated_at', 'vacancy', 'ships']

    def get_validation_exclusions(self):
        exclusions = super(MotherShipDetailsSerializer, self).get_validation_exclusions()
        return exclusions + ['id', 'created_at,', 'updated_at', 'vacancy']
