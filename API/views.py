from django.shortcuts import render
from rest_framework import viewsets
from .serializer import DatosSerializer
from .models import Datos


class VistaTareas(viewsets.ModelViewSet):
    serializer_class = DatosSerializer
    queryset = Datos.objects.all()
