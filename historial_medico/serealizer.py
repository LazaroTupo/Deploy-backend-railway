from rest_framework import serializers
from .models import Trastornos
from .models import ExamenFisico
from .models import Observaciones
from .models import EvaluacionCorporal
from .models import DolorInfo
from .models import Antecedentes
from .models import Evaluacion

class TrastornosSerealizer(serializers.ModelSerializer):
    class Meta:
        #clase
        model = Trastornos
        #campos
        fields = '__all__'

class ExamenFisicoSerealizer(serializers.ModelSerializer):
    class Meta:
        #clase
        model = ExamenFisico
        #campos
        fields = '__all__'

class ObservacionesSerealizer(serializers.ModelSerializer):
    class Meta:
        #clase
        model = Observaciones
        #campos
        fields = '__all__'


class EvaluacionCorporalSerializer(serializers.ModelSerializer):
    class Meta:
        model = EvaluacionCorporal
        fields = '__all__'
    
class DolorInfoSerializer(serializers.ModelSerializer):
    class Meta:
        model = DolorInfo
        fields = '__all__'
        
class AntecedentesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Antecedentes
        fields = '__all__'
        
class EvaluacionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Evaluacion
        fields = '__all__'



