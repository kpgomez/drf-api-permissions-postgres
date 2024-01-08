from rest_framework import generics
from .models import Toy
from .permissions import IsOwnerOrReadOnly
from .serializers import ToySerializer


class ToyList(generics.ListCreateAPIView):
    permission_classes = [IsOwnerOrReadOnly, ]
    queryset = Toy.objects.all()
    serializer_class = ToySerializer


class ToyDetail(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = [IsOwnerOrReadOnly, ]
    queryset = Toy.objects.all()
    serializer_class = ToySerializer
