from  rest_framework.serializers import  ModelSerializer
from  App.Catalogo.Salida.models import Salida

class SalidaSerialize(ModelSerializer):
    class Meta:
        model = Salida
        fields = ['id','tiposalida_id', 'fechasalida']