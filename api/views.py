from django.http import Http404
from drf_yasg.utils import swagger_auto_schema
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

from api import services, swagger
from api.models import Crew, MotherShip, Ship
from api.serializers import (CrewDetailsSerializer, CrewSerializer,
                             MotherShipDetailsSerializer, MotherShipSerializer,
                             ShipDetailsSerializer, ShipSerializer)
from api.services import swap_crew
from api.utils.exception_handlers import InvalidQueryParameters


class MotherShipList(APIView):

    @swagger_auto_schema(operation_id='Mothership List')
    def get(self, request):
        mothership = MotherShip.objects.all()
        serializer = MotherShipSerializer(mothership, many=True)
        return Response(serializer.data)

    @swagger_auto_schema(operation_id='Mothership Create')
    def post(self, request):
        serializer = MotherShipSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class MotherShipDetails(APIView):

    def get_object(self, pk):
        try:
            return MotherShip.objects.get(pk=pk)
        except MotherShip.DoesNotExist:
            raise Http404

    @swagger_auto_schema(operation_id='Mothership Details')
    def get(self, request, pk):
        mothership = self.get_object(pk)
        serializer = MotherShipDetailsSerializer(mothership)
        return Response(serializer.data)

    @swagger_auto_schema(operation_id='Mothership Delete')
    def delete(self, request, pk):
        mothership = self.get_object(pk)
        mothership.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


# Ship Views

class ShipList(APIView):

    @swagger_auto_schema(operation_id='Ship List')
    def get(self, request):
        ship = Ship.objects.all()
        serializer = ShipSerializer(ship, many=True)
        return Response(serializer.data)

    @swagger_auto_schema(request_body=swagger.ship_create_schema, operation_id='Ship Create')
    def post(self, request):
        count = request.data.get('count')
        if count:
            count = int(count)
            mothership_id = request.data.get('mothership')
            services.validate_mothership_vacancy(mothership_id, count)
            ships = []
            for i in range(count):
                serializer = ShipSerializer(data={'mothership': mothership_id})
                if serializer.is_valid():
                    serializer.save()
                    ships.append(serializer.data)
            return Response(ships, status=status.HTTP_201_CREATED)
        serializer = ShipSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class ShipDetails(APIView):

    def get_object(self, pk):
        try:
            return Ship.objects.get(pk=pk)
        except Ship.DoesNotExist:
            raise Http404

    @swagger_auto_schema(operation_id='Ship Details')
    def get(self, request, pk):
        ship = self.get_object(pk)
        serializer = ShipDetailsSerializer(ship)
        return Response(serializer.data)

    @swagger_auto_schema(operation_id='Ship Delete')
    def delete(self, request, pk):
        ship = self.get_object(pk)
        ship.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


# Crew Views

class CrewList(APIView):

    @swagger_auto_schema(operation_id='Crew List')
    def get(self, request):
        crew = Crew.objects.all()
        serializer = CrewSerializer(crew, many=True)
        return Response(serializer.data)

    @swagger_auto_schema(request_body=swagger.crew_create_schema, operation_id='Crew Create')
    def post(self, request):
        serializer = CrewSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    @swagger_auto_schema(request_body=swagger.crew_swap_schema, operation_id='Crew Swap')
    def put(self, request):
        try:
            from_ship_id = request.data['from_ship']
            to_ship_id = request.data['to_ship']
            name = request.data['name']
        except KeyError:
            raise InvalidQueryParameters()
        crew = swap_crew(from_ship_id, to_ship_id, name)
        serializer = CrewSerializer(crew)
        return Response(serializer.data, status=status.HTTP_202_ACCEPTED)


class CrewDetails(APIView):

    def get_object(self, pk):
        try:
            return Crew.objects.get(pk=pk)
        except Crew.DoesNotExist:
            raise Http404

    @swagger_auto_schema(operation_id='Crew Details')
    def get(self, request, pk):
        crew = self.get_object(pk)
        serializer = CrewDetailsSerializer(crew)
        return Response(serializer.data)

    @swagger_auto_schema(operation_id='Crew Delete')
    def delete(self, request, pk):
        crew = self.get_object(pk)
        crew.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
