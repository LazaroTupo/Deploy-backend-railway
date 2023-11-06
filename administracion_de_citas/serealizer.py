from rest_framework import serializers
from .models import Terapista
from .models import Paciente
from .models import Cita

class TerapistaSerealizer(serializers.ModelSerializer):
    class Meta:
        model = Terapista
        fields = '__all__'
        
class PacienteSerealizer(serializers.ModelSerializer):
    class Meta:
        model = Paciente
        fields = '__all__'

class CitaSerealizer(serializers.ModelSerializer):
    class Meta:
        model = Cita
        fields = '__all__'
