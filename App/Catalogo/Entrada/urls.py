from django.urls import  path, include
from rest_framework.routers import  DefaultRouter


from .ApiView import EntradaApiView
from .ModelViewSet import EntradaViewSet

from .models import Entrada
from ...Detalles.DetalleEntrada.models import DetalleEntrada

router = DefaultRouter()
router.register(r'entrada',EntradaViewSet, basename='entrada')



urlpatterns = [

    path('', include(router.urls)),

]