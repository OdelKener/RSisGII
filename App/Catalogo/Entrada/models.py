from django.db import models

from App.Catalogo.TipoEntrada.models import TipoEntrada

from Paises.Nicaragua.models import Sucursal
from Paises.Panama.models import SucursalPan
from Paises.Hondura.models import SucursalHon
from Paises.CostaRica.models import SucursalCos

class Entrada(models.Model):
    fechaentrada = models.CharField(verbose_name='FechaEntrada', max_length=100)

    tipoentrada  = models.ForeignKey(TipoEntrada, verbose_name='TipoEntrada', on_delete=models.PROTECT)

    sucursalid = models.ForeignKey(Sucursal,verbose_name='Sucursal', on_delete=models.PROTECT, null=True, blank=True)
    sucursalidcos = models.ForeignKey(SucursalCos,verbose_name='SucursalCos', on_delete=models.PROTECT, null=True, blank=True)
    sucursalidhon = models.ForeignKey(SucursalHon,verbose_name='SucursalHon', on_delete=models.PROTECT, null=True, blank=True)
    sucursalidpan = models.ForeignKey(SucursalPan,verbose_name='SucursalPan', on_delete=models.PROTECT, null=True, blank=True)







# Create your models here.
# Create your models here.
