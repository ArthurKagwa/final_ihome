from django.shortcuts import render
from django.http import HttpResponse
from rest_framework.authentication import TokenAuthentication
from rest_framework.decorators import action
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.views import APIView
from rest_framework.viewsets import ModelViewSet
from rest_framework.response import Response
from rest_framework import status

# Create your views here.

from .models import Animal, Breed, Type, Staff, Event, Task, Farm
from .serializers import AnimalSerializer, BreedSerializer, TypeSerializer, StaffSerializer, EventSerializer, \
    TaskSerializer, FarmSerializer


class AnimalViewSet(ModelViewSet):
    queryset = Animal.objects.all()
    serializer_class = AnimalSerializer

    @action(detail=False, methods=['get'])
    def by_type_and_farm(self, request):
        type_id = request.query_params.get('type_id')
        farm_id = request.query_params.get('farm_id')
        try:
            type_instance = Type.objects.get(pk=type_id)
            farm_instance = Farm.objects.get(pk=farm_id)
            animals = Animal.objects.filter(type=type_instance, farm=farm_instance)
            serializer = AnimalSerializer(animals, many=True)
            return Response(serializer.data)
        except Type.DoesNotExist:
            return Response({"error": "Type not found"}, status=404)
        except Farm.DoesNotExist:
            return Response({"error": "Farm not found"}, status=404)

class BreedViewSet(ModelViewSet):
    queryset = Breed.objects.all()
    serializer_class = BreedSerializer

    @action(detail=True, methods=['get'])
    def by_type(self, request, pk=None):
        try:
            type_instance = Type.objects.get(pk=pk)
            breeds = Breed.objects.filter(animal_type=type_instance)
            serializer = BreedSerializer(breeds, many=True)
            return Response(serializer.data)
        except Type.DoesNotExist:
            return Response({"error": "Type not found"}, status=404)

    @action(detail=False, methods=['get'])
    def by_type_and_farm(self, request):
        type_id = request.query_params.get('type_id')
        farm_id = request.query_params.get('farm_id')
        try:
            type_instance = Type.objects.get(pk=type_id)
            farm_instance = Farm.objects.get(pk=farm_id)
            breeds = Breed.objects.filter(animal_type=type_instance, farm=farm_instance)
            serializer = BreedSerializer(breeds, many=True)
            return Response(serializer.data)
        except Type.DoesNotExist:
            return Response({"error": "Type not found"}, status=404)
        except Farm.DoesNotExist:
            return Response({"error": "Farm not found"}, status=404)

class TypeViewSet(ModelViewSet):
    queryset = Type.objects.all()
    serializer_class = TypeSerializer

class StaffViewSet(ModelViewSet):
    queryset = Staff.objects.all()
    serializer_class = StaffSerializer

def home(request):
    return HttpResponse('Welcome to the Animal  API')

class EventViewSet(ModelViewSet):
    queryset = Event.objects.all()
    serializer_class = EventSerializer

class TaskViewSet(ModelViewSet):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer


#farm viewset
class FarmViewSet(ModelViewSet):
    queryset = Farm.objects.all()
    serializer_class = FarmSerializer
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]

    def perform_create(self, serializer):
        try:
            serializer.save(owner=self.request.user)
        except serializer.ValidationError as e:
            return Response({"error": str(e)}, status=status.HTTP_400_BAD_REQUEST)
    def get_queryset(self):
        return Farm.objects.filter(owner=self.request.user)
    #getting individual farm details





