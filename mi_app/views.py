from rest_framework import viewsets
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.contrib import messages
from .serializer import CitaSerializer
from .serializer import MedicoSerializer
from .serializer import PacienteSerializer
from .serializer import PruebaMedicaSerializer
from .serializer import TratamientoSerializer
from .models import Cita
from .models import Medico
from .models import Paciente
from .models import PruebaMedica
from .models import Tratamiento 
from django.views.generic import ListView, DetailView, UpdateView, CreateView

# Create your views here.
class CitaView(viewsets.ModelViewSet):
    serializer_class = CitaSerializer
    queryset = Cita.objects.all()

# class MedicoView(viewsets.ModelViewSet):
#     serializer_class = MedicoSerializer
#     queryset = Medico.objects.all()

class PacienteView(viewsets.ModelViewSet):
    serializer_class = PacienteSerializer
    queryset = Paciente.objects.all()

class PruebaMedicaView(viewsets.ModelViewSet):
    serializer_class = PruebaMedicaSerializer
    queryset = PruebaMedica.objects.all()

class TratamientoView(viewsets.ModelViewSet):
    serializer_class = TratamientoSerializer
    queryset = Tratamiento.objects.all()

def index_view(request):
    return render(request, 'index.html')

def paciente_view(request):
    return render(request, 'paciente.html')

def medico_view(request):
    listado = ['manzana', 'banana']

    return render(request, 'medico.html',context={'listado':listado, 'user':request.user})

def iniciar_sesion(request):
    if request.method == 'post':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            # Verifica si el usuario es un médico
            if Medico.objects.filter(user=user).exists():
                return redirect('medico')  # Cambia 'ruta-medico' por la ruta real para médicos
            # Verifica si el usuario es un paciente
            elif Paciente.objects.filter(user=user).exists():
                return redirect('paciente')  # Cambia 'ruta-paciente' por la ruta real para pacientes
            else:
                messages.error(request, 'Usuario no tiene un rol válido.')
        else:
            messages.error(request, 'Credenciales inválidas. Inténtalo de nuevo.')
    return render(request, 'registration/login.html')