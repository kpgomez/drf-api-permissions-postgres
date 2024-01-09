from rest_framework import generics
from .models import Wishlist
from .serializers import WishlistSerializer
from .permissions import IsOwnerOrReadOnly


# Create your views here.
class WishlistList(generics.ListCreateAPIView):
    queryset = Wishlist.objects.all()
    serializer_class = WishlistSerializer


class WishlistDetail(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = [IsOwnerOrReadOnly, ]
    queryset = Wishlist.objects.all()
    serializer_class = WishlistSerializer
