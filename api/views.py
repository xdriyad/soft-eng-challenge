from django.shortcuts import render
from django.http import Http404
from api.models import MotherShip, Ship, Crew
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from api.serializers import MotherShipSerializer, MotherShipDetailsSerializer, ShipSerializer, ShipDetailsSerializer, \
    CrewDetailsSerializer, CrewSerializer


class MotherShipList(APIView):
    """
    List all mother_ship, or create a new snippet.
    """
    def get(self, request):
        mother_ship = MotherShip.objects.all()
        serializer = MotherShipSerializer(mother_ship, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = MotherShipSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
class MotherShipDetails(APIView):
    """
    Retrieve, update or delete a mother_ship instance.
    """
    def get_object(self, pk):
        try:
            return MotherShip.objects.get(pk=pk)
        except MotherShip.DoesNotExist:
            raise Http404

    def get(self, request, pk):
        mother_ship = self.get_object(pk)
        serializer = MotherShipDetailsSerializer(mother_ship)
        return Response(serializer.data)

    def put(self, request, pk):
        mother_ship = self.get_object(pk)
        serializer = MotherShipDetailsSerializer(mother_ship, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        mother_ship = self.get_object(pk)
        mother_ship.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

# Ship Views


class ShipList(APIView):
    """
    List all ship, or create a new snippet.
    """

    def get(self, request):
        ship = Ship.objects.all()
        serializer = ShipSerializer(ship, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = ShipSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class ShipDetails(APIView):
    """
    Retrieve, update or delete a ship instance.
    """

    def get_object(self, pk):
        try:
            return Ship.objects.get(pk=pk)
        except Ship.DoesNotExist:
            raise Http404

    def get(self, request, pk):
        ship = self.get_object(pk)
        serializer = ShipDetailsSerializer(ship)
        return Response(serializer.data)

    def put(self, request, pk):
        ship = self.get_object(pk)
        serializer = ShipDetailsSerializer(ship, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        ship = self.get_object(pk)
        ship.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

# Crew Views


class CrewList(APIView):
    """
    List all crew, or create a new snippet.
    """

    def get(self, request):
        crew = Crew.objects.all()
        serializer = CrewSerializer(crew, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = CrewSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class CrewDetails(APIView):
    """
    Retrieve, update or delete a crew instance.
    """

    def get_object(self, pk):
        try:
            return Crew.objects.get(pk=pk)
        except Crew.DoesNotExist:
            raise Http404

    def get(self, request, pk):
        crew = self.get_object(pk)
        serializer = CrewDetailsSerializer(crew)
        return Response(serializer.data)

    def put(self, request, pk):
        crew = self.get_object(pk)
        serializer = CrewDetailsSerializer(crew, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        crew = self.get_object(pk)
        crew.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)