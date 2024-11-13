from rest_framework.viewsets import ModelViewSet
from .models import  Entrada
from .Serializer import EntradaSerialize
from App.Detalles.DetalleEntrada.Serializer import DetalleEntradaSerialize

class EntradaViewSet(ModelViewSet):
    queryset = Entrada.objects.all()
    serializer_class = EntradaSerialize

