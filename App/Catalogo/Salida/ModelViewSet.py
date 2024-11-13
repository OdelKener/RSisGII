from rest_framework.viewsets import ModelViewSet
from .models import  Salida
from .Serializer import SalidaSerialize
from App.Detalles.DetalleSalida.Serializer import DetalleSalidaSerialize
from ...Detalles.DetalleSalida.models import DetalleSalida

class SalidaViewSet(ModelViewSet):
    queryset = Salida.objects.all()
    serializer_class = SalidaSerialize


    querysetd = DetalleSalida.objects.all()
    serializer_classd = DetalleSalidaSerialize

