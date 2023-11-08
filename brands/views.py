from django.shortcuts import render
from .models import Cloths
from .serializers import ClotheSerializers
from rest_framework import viewsets


# Create your views here.

class ClothsView(viewsets.ModelViewSet):
    queryset = Cloths.objects.all()
    serializer_class = ClotheSerializers