from rest_framework import serializers

from api import models, services


class CrewSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Crew
        fields = ('id', 'name', 'ship',)

    def get_validation_exclusions(self):
        exclusions = super(CrewSerializer, self).get_validation_exclusions()
        return exclusions + ['id', 'created_at,', 'updated_at']

    def create(self, validated_data):
        return services.create_crew(validated_data['ship'], name=validated_data['name'])


class ShipSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Ship
        fields = ('id', 'mothership')

    def get_validation_exclusions(self):
        exclusions = super(ShipSerializer, self).get_validation_exclusions()
        return exclusions + ['id', 'created_at,', 'updated_at']

    def create(self, validated_data):
        return services.create_ship(validated_data['mothership'])


class CrewDetailsSerializer(serializers.ModelSerializer):
    ship = ShipSerializer()

    class Meta:
        model = models.Crew
        fields = ('id', 'name', 'created_at', 'updated_at', 'ship',)

    def get_validation_exclusions(self):
        exclusions = super(CrewDetailsSerializer, self).get_validation_exclusions()
        return exclusions + ['id', 'created_at,', 'updated_at']


class MotherShipSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.MotherShip
        fields = ('id',)

    def get_validation_exclusions(self):
        exclusions = super(MotherShipSerializer, self).get_validation_exclusions()
        return exclusions + ['id', 'created_at,', 'updated_at']

    def create(self, validated_data):
        return services.create_mothership()


class ShipDetailsSerializer(serializers.ModelSerializer):
    crew = CrewSerializer(source='crew_set', many=True)
    mothership = MotherShipSerializer()

    class Meta:
        model = models.Ship
        fields = ('id', 'created_at', 'mothership', 'vacancy', 'crew',)

    def get_validation_exclusions(self):
        exclusions = super(ShipDetailsSerializer, self).get_validation_exclusions()
        return exclusions + ['id', 'created_at,', 'updated_at']


class MotherShipDetailsSerializer(serializers.ModelSerializer):
    ships = ShipSerializer(source='ship_set', many=True)

    class Meta:
        model = models.MotherShip
        fields = ('id', 'created_at', 'updated_at', 'vacancy', 'ships',)

    def get_validation_exclusions(self):
        exclusions = super(MotherShipDetailsSerializer, self).get_validation_exclusions()
        return exclusions + ['id', 'created_at,', 'updated_at', 'vacancy']
