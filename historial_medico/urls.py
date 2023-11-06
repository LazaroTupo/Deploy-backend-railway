from django.urls import path, include
from rest_framework import routers
from .views import TrastornosView
from .views import ExamenFisicoView
from .views import ObservacionesView
from .views import EvaluacionCorporalView
from .views import DolorInfoView
from .views import AntecedentesView
from .views import EvaluacionView

#ESPACIO DE ROUTERS
router_01 = routers.DefaultRouter()
router_01.register(r'trastornos',TrastornosView,'trastornos') #view.TrastornoView

router_02 = routers.DefaultRouter()
router_02.register(r'examenFisico',ExamenFisicoView,'examen fisico')

router_03 = routers.DefaultRouter()
router_03.register(r'observaciones',ObservacionesView,'observaciones')

#ESPACIO DE ROUTERS
router1 = routers.DefaultRouter()
router1.register(r'evaluacionCorporal',EvaluacionCorporalView,'evaluacionCorporal')

router2 = routers.DefaultRouter()
router2.register(r'dolorInfo',DolorInfoView,'dolorInfo')

router3 = routers.DefaultRouter()
router3.register(r'antecedentes',AntecedentesView,'antecedente')

router4 = routers.DefaultRouter()
router4.register(r'evaluacion',EvaluacionView,'evaluacion')

urlpatterns = [
    path("",include(router_01.urls)),
    path("",include(router_02.urls)),
    path("",include(router_03.urls)),
    path("",include(router1.urls)),
    path("",include(router2.urls)),
    path("",include(router3.urls)),
    path("",include(router4.urls))
]

