from django.shortcuts import render
from rest_framework import viewsets
from app01.serializers import ToDoSerializer
from app01.models import ToDo
# Create your views here.
class ToDoViewSet(viewsets.ModelViewSet):
    queryset = ToDo.objects.all()
    serializer_class = ToDoSerializer
