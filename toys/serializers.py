from rest_framework import serializers
from .models import Toy  # the model that needs to be serialized as JSON


class ToySerializer(serializers.ModelSerializer):
    class Meta:
        fields = ("id", "purchaser", "title", "description", "created_at", "last_modified")
        model = Toy
