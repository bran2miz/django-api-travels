from django.shortcuts import render
from rest_framework import generics
from .serializer import TravelSerializer
from .models import Travel

class TravelList(generics.ListCreateAPIView):
  queryset = Travel.objects.all()
  serializer_class = TravelSerializer

class TravelDetail(generics.RetrieveUpdateDestroyAPIView):
  queryset = Travel.objects.all()
  serializer_class = TravelSerializer