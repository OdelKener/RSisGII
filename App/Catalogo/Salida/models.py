from django.db import models

from App.Catalogo.TipoSalida.models import TipoSalida
from App.Paises.Nicaragua.models import Sucursal
from App.Paises.Panama.models import SucursalPan
from App.Paises.Hondura.models import SucursalHon
from App.Paises.CostaRica.models import SucursalCos


class Salida(models.Model):
    fechasalida = models.CharField(verbose_name='FechaSalida', max_length=100)

    tiposalida= models.ForeignKey(TipoSalida, verbose_name='TipoSalida', on_delete=models.PROTECT)

    sucursalid = models.ForeignKey(Sucursal, verbose_name='Sucursal', on_delete=models.PROTECT, null=True, blank=True)
    sucursalidcos = models.ForeignKey(SucursalCos, verbose_name='Sucursalcos', on_delete=models.PROTECT, null=True, blank=True)
    sucursalidhon = models.ForeignKey(SucursalHon, verbose_name='SucursalHon', on_delete=models.PROTECT, null=True, blank=True)
    sucursalidpan = models.ForeignKey(SucursalPan, verbose_name='SucursalPan', on_delete=models.PROTECT, null=True, blank=True)


class Meta:
    verbose_name = 'Salidas'

def __str__(self):
    return f'{self.fechasalida},{self.tiposalida},{self.sucursalidcos},{self.sucursalidhon},{self.sucursalidpan}'

# Create your models here.
