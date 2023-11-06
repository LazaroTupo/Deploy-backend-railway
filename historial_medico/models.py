from django.db import models

class Trastornos(models.Model): #maylle
    # atributos
    vasculares = models.CharField(max_length=100, null = True, blank = True)
    afasia = models.CharField(max_length=15, null = True, blank = True)
    disartria = models.CharField(max_length=15, null = True, blank = True)
    disfagia = models.BooleanField()
    disfonia = models.CharField(max_length=15, null = True, blank = True)

class ExamenFisico(models.Model): #maylle
    # atributos
    grado_funcional = models.CharField(max_length=20, null = True, blank = True)
    actitud_postural = models.CharField(max_length=20, null = True, blank = True)
    reflejos = models.CharField(max_length=20, null = True, blank = True)
    actividades_motoras = models.CharField(max_length=100, null = True, blank = True, verbose_name="Actividades motrices")
    coordinacion = models.CharField(max_length=20, null = True, blank = True, verbose_name="Equilibrio y coordinación")
    orientacion = models.CharField(max_length=20, null = True, blank = True, verbose_name="Orientación")

class Observaciones(models.Model): #maylle
    # atributos
    traqueostomia = models.BooleanField()
    upp = models.BooleanField()
    control_esfinteres = models.BooleanField()
    sentidos = models.CharField(max_length=50, null = True, blank = True)
    estado_de_animo = models.CharField(max_length=20, null = True, blank = True)
    pruebas_especiales = models.CharField(max_length=50, null = True, blank = True)
    ayuda_diagnosticada = models.CharField(max_length=50, null = True, blank = True)

class EvaluacionCorporal(models.Model):
    # atributos
    esquema_corporal = models.CharField(max_length=100, null = True, blank = True)
    sensibilidad_superficial = models.CharField(max_length=15, null = True, blank = True)
    sensibilidad_profunda = models.CharField(max_length=15, null = True, blank = True)
    nivel_fuerza = models.IntegerField(null = True, blank = True)
    tono_muscular = models.CharField(max_length=20, null = True, blank = True)
    trofismo_muscular = models.CharField(max_length=15, null = True, blank = True)
    rangos_articulares = models.CharField(max_length=100, null = True, blank = True)
    retracciones_musculares = models.CharField(max_length=100, null = True, blank = True)

class DolorInfo(models.Model):
    # atributos
    grado_de_enfermedad = models.CharField(max_length=30, null = True, blank = True)
    nivel = models.IntegerField(verbose_name="Grado de dolor",  null = True, blank=True)
    area = models.CharField(max_length=100, null = True, blank = True, verbose_name="Zona de dolor")
    palpacion = models.BooleanField(verbose_name="Dolor a la palpitación")
    punto_gatillo = models.CharField(max_length=100, null = True, blank = True)    
    distribucion = models.CharField(max_length=20, null = True, blank = True, verbose_name="Distribución del dolor")
    ocurrencia = models.CharField(max_length=50, null = True, blank = True)

class Antecedentes(models.Model):
    # atributos
    diabetes = models.BooleanField()
    diabetes_tipo = models.CharField(max_length=10,verbose_name="Tipo", blank=True, null=True)
    hta = models.BooleanField()
    hta_tipo = models.CharField(max_length=50,verbose_name="HTA", blank=True, null=True)
    cardiaco = models.BooleanField()
    cardiaco_tipo = models.CharField(max_length=50,verbose_name="Antecedentes Cardiacos", blank=True, null=True)
    respiratorio = models.BooleanField()
    respiratorio_tipo = models.CharField(max_length=100,verbose_name="Antecedentes Respiratorios", blank=True, null=True)
    operaciones = models.BooleanField()
    operaciones_tipo = models.CharField(max_length=100,verbose_name="Operaciones", blank=True, null=True)
    otros = models.CharField(max_length=200, null = True, blank = True)
    alergias = models.CharField(max_length=200, null = True, blank = True)

class Evaluacion(models.Model):
    # atributos
    fecha = models.DateField(null = True, blank = True)
    paciente = models.ForeignKey('administracion_de_citas.Paciente', on_delete=models.CASCADE) #Unico con llave Foranea       
    dado_de_alta = models.BooleanField(blank=True, verbose_name="Paciente dado de alta")
    enfermedad_actual = models.CharField(max_length=100, null = True, blank = True)
    tiempo_enfermedad = models.CharField(max_length=30)
    diagnostico_medico = models.CharField(max_length=100, null = True, blank = True)
    diagnostico_terapeutico = models.CharField(max_length=100, null = True, blank = True)
    medicamentos = models.CharField(max_length=100, null=True, blank=True)
    antecedentes = models.OneToOneField(Antecedentes, on_delete=models.CASCADE) #De 1 a 1
    examen_fisico = models.OneToOneField(ExamenFisico, on_delete=models.CASCADE)
    dolor_info = models.OneToOneField(DolorInfo, on_delete=models.CASCADE)
    evaluacion_corporal = models.OneToOneField(EvaluacionCorporal, on_delete=models.CASCADE)
    trastornos = models.OneToOneField(Trastornos, on_delete=models.CASCADE)
    consideraciones = models.OneToOneField(Observaciones, on_delete=models.CASCADE)
    plan_de_tratamiento = models.TextField(null = True, blank = True)
    observaciones_y_consideraciones = models.TextField(null = True, blank = True)
    
    