from django.contrib import admin
from .models import Cita
from .models import Paciente
from .models import Medico
from .models import PruebaMedica
from .models import Tratamiento

# Register your models here.
admin.site.register(Cita)
admin.site.register(Paciente)
admin.site.register(Medico)
admin.site.register(PruebaMedica)
admin.site.register(Tratamiento)