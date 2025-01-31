from rest_framework import serializers
from Farm.models import Farm, Staff, Animal, Breed, Type, Event, Task, Medical
from django.contrib.auth.models import User

class FarmSerializer(serializers.ModelSerializer):
    class Meta:
        model = Farm
        fields = ['phone_number','location','email','name',]

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['username','email','password']

