from rest_framework import serializers
from .models import Puppy

# Create the Serializer Class


class PuppySerializer(serializers.ModelSerializer):
    class Meta:
        model = Puppy
        fields = '__all__'

# Path: puppy_store\puppies\views.py
