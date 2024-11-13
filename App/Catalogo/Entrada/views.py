from django.shortcuts import render

# Create your views here.
from rest_framework.permissions import IsAuthenticated
from rest_framework.views import APIView
from .models import Entrada
from .Serializer import EntradaSerialize



class EntradaView( APIView):
    permission_classes = [IsAuthenticated]
    queryset = Entrada.objects.all()
    serializer_class = EntradaSerialize

