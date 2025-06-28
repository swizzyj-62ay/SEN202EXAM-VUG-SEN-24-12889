from django.shortcuts import render
from rest_framework import viewsets
from .models import Manager, Intern
from .serializers import ManagerSerializer, InternSerializer

class ManagerViewSet(viewsets.ModelViewSet):
    queryset = Manager.objects.all()
    serializer_class = ManagerSerializer

class InternViewSet(viewsets.ModelViewSet):
    queryset = Intern.objects.all()
    serializer_class = InternSerializer

# Create your views here.
