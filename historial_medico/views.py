
from django.shortcuts import render
from rest_framework import viewsets
from .serealizer import TrastornosSerealizer
from .models import Trastornos
from .serealizer import ExamenFisicoSerealizer
from .models import ExamenFisico
from .serealizer import ObservacionesSerealizer
from .models import Observaciones
from .serealizer import EvaluacionCorporalSerializer
from .serealizer import DolorInfoSerializer
from .serealizer import AntecedentesSerializer
from .serealizer import EvaluacionSerializer
from .models import EvaluacionCorporal
from .models import DolorInfo
from .models import Antecedentes
from .models import Evaluacion


class TrastornosView(viewsets.ModelViewSet):
    #indicamos la clase serializada
    serializer_class = TrastornosSerealizer
    #guardamos todos los objetos del modelo
    queryset = Trastornos.objects.all()

class ExamenFisicoView(viewsets.ModelViewSet):
    #indicamos la clase serializada
    serializer_class = ExamenFisicoSerealizer
    #guardamos todos los objetos del modelo
    queryset = ExamenFisico.objects.all()

class ObservacionesView(viewsets.ModelViewSet):
    #indicamos la clase serializada
    serializer_class = ObservacionesSerealizer
    #guardamos todos los objetos del modelo
    queryset = Observaciones.objects.all()
    

class EvaluacionCorporalView(viewsets.ModelViewSet):
    serializer_class = EvaluacionCorporalSerializer
    queryset = EvaluacionCorporal.objects.all()
    
class DolorInfoView(viewsets.ModelViewSet):
    serializer_class=DolorInfoSerializer
    queryset = DolorInfo.objects.all()
    
class AntecedentesView(viewsets.ModelViewSet):
    serializer_class=AntecedentesSerializer
    queryset = Antecedentes.objects.all()

class EvaluacionView(viewsets.ModelViewSet):
    serializer_class=EvaluacionSerializer
    queryset = Evaluacion.objects.all()
    
