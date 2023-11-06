from rest_framework import viewsets
from .serealizer import TerapistaSerealizer
from .models import Terapista
from .serealizer import PacienteSerealizer
from .models import Paciente
from .models import Cita
from .serealizer import CitaSerealizer

class TerapistaView(viewsets.ModelViewSet):
    #Indicamos clase Serializada
    serializer_class = TerapistaSerealizer
    #Guardamos todos los objetos del modelo
    queryset = Terapista.objects.all()
    
class PacienteView(viewsets.ModelViewSet):
    #Clase a Serializar
    serializer_class = PacienteSerealizer
    #Guardamos todos los objetos del modelo
    queryset = Paciente.objects.all()

class CitaView(viewsets.ModelViewSet):
    #Clase a Serializar
    serializer_class = CitaSerealizer
    #Guardamos todos los objetos del modelo
    queryset = Cita.objects.all()    


























#from .models import Paciente
#from django.http import JsonResponse

#def getPacientes(request):
#    pacientes = list(Paciente.objects.all())
#    json = {}
#    for i in pacientes:
#        json[i.dni] = {
#            "nombre" : i.nombre,
#            "apellido" : i.apellido
#        }
#    return JsonResponse(json)