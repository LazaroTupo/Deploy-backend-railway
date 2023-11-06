from django.urls import path, include
from rest_framework import routers
from .views import *
from .views import CitaView

#ESPACIO DE ROUTERS
router1 = routers.DefaultRouter()
router1.register(r'terapista',TerapistaView,'terapista')

router2 = routers.DefaultRouter()
router2.register(r'paciente', PacienteView, 'paciente')

router3 = routers.DefaultRouter()
router3.register(r'cita',CitaView,'cita')

#ESPACIO DE URL
urlpatterns = [
    #path (Ruta , urlGeneradaPorRouter)
    path("",include(router1.urls)),
    path("",include(router2.urls)),
    path("",include(router3.urls))
]


