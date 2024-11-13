from  rest_framework.serializers import  ModelSerializer
from  App.Catalogo.Entrada.models import Entrada

class EntradaSerialize(ModelSerializer):
    class Meta:
        model = Entrada
        fields = [ 'fechaentrada','sucursalid_id','tipoentrada_id',]