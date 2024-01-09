from rest_framework import serializers
from .models import Wishlist


class WishlistSerializer(serializers.ModelSerializer):
    class Meta:
        fields = ("id", "owner", "toys")
        model = Wishlist
