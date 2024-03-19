from rest_framework import serializers
from .models import Cita
from .models import Medico
from .models import Paciente
from .models import PruebaMedica
from .models import Tratamiento

class CitaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cita
        fields = '__all__'

class PacienteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Paciente
        fields = '__all__'

class MedicoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Medico
        fields = '__all__'

class PruebaMedicaSerializer(serializers.ModelSerializer):
    class Meta:
        model = PruebaMedica
        fields = '__all__'

class TratamientoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tratamiento
        fields = '__all__'