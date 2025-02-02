from django.contrib.auth import authenticate
from rest_framework import serializers

from .models import Animal, Breed, Type, Staff, Event, Task, AbstractUser, Farm

class TypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Type
        fields = ['name', 'desc']

class BreedSerializer(serializers.ModelSerializer):
    class Meta:
        model = Breed
        fields = '__all__'

class AnimalSerializer(serializers.ModelSerializer):
    class Meta:
        model = Animal
        fields = '__all__'

class StaffSerializer(serializers.ModelSerializer):
    class Meta:
        model = Staff
        fields = '__all__'

class EventSerializer(serializers.ModelSerializer):
    class Meta:
        model = Event
        fields = '__all__'

class TaskSerializer(serializers.ModelSerializer):
    class Meta:
        model = Task
        fields = '__all__'


#farm serializer
class FarmSerializer(serializers.ModelSerializer):
    class Meta:
        model = Farm
        fields =( 'name','location','phone_number','email', 'owner','id')

