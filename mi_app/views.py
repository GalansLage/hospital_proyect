# from rest_framework import viewsets
from django.shortcuts import render, redirect
from django.urls import reverse
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from django.contrib import messages
# from .serializer import CitaSerializer
# from .serializer import MedicoSerializer
# from .serializer import PacienteSerializer
# from .serializer import PruebaMedicaSerializer
# from .serializer import TratamientoSerializer
from .models import Cita
from .models import Medico
from .models import Paciente
from .models import PruebaMedica
from .models import Tratamiento 
from django.views.generic import ListView, DetailView, UpdateView, CreateView

# Create your views here.
# class CitaView(viewsets.ModelViewSet):
#     serializer_class = CitaSerializer
#     queryset = Cita.objects.all()

# # class MedicoView(viewsets.ModelViewSet):
# #     serializer_class = MedicoSerializer
# #     queryset = Medico.objects.all()

# class PacienteView(viewsets.ModelViewSet):
#     serializer_class = PacienteSerializer
#     queryset = Paciente.objects.all()

# class PruebaMedicaView(viewsets.ModelViewSet):
#     serializer_class = PruebaMedicaSerializer
#     queryset = PruebaMedica.objects.all()

# class TratamientoView(viewsets.ModelViewSet):
#     serializer_class = TratamientoSerializer
#     queryset = Tratamiento.objects.all()

def index_view(request):
    return render(request, 'index.html')

@login_required(login_url='index')
def paciente_view(request, pk):
    try:
        paciente = Paciente.objects.get(pk=pk)
    except Paciente.DoesNotExist():
        return render(request, 'index.html', context={'error', True})

    return render(request, 'paciente.html', {'paciente':paciente})

def medico_view(request, pk):
    """Este es el detalle medico"""
    medico = Medico.objects.get(pk=pk)
    return render(request, 'medico.html',context={'medico':medico})

def iniciar_sesion(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            # Verifica si el usuario es un médico
            if Medico.objects.filter(user=user).exists():
                medico = Medico.objects.filter(user=user)[0]
                return redirect(reverse('medico', kwargs={'pk': medico.pk}) ) # Cambia 'ruta-medico' por la ruta real para médicos
            # Verifica si el usuario es un paciente
            elif Paciente.objects.get(user=user):
                paciente = Paciente.objects.filter(user=user)[0]
                return redirect(reverse('paciente', kwargs={'pk': paciente.pk}) ) # Cambia 'ruta-paciente' por la ruta real para pacientes
            else:
                messages.error(request, 'Usuario no tiene un rol válido.')
        else:
            messages.error(request, 'Credenciales inválidas. Inténtalo de nuevo.')
    return render(request, 'registration/login.html')


########### PACIENTE CRUD ##################
@login_required()
def update_paciente(request, pk):
    # print(request.POST.get('nombre'))
    if request.method == 'POST':
        try:
            # print('igkushdbkushd',request.POST.get('genero'))
            paciente = Paciente.objects.get(pk = pk)
            fecha = request.POST.get('fecha_Nacimiento')
            # print(fecha)
            paciente.nombre = request.POST.get('nombre')
            paciente.apellido = request.POST.get('apellido')
            # paciente.fecha_Nacimiento = fecha
            # paciente.genero = request.POST.get('genero')
            paciente.email = request.POST.get('email')
            paciente.save()

            return render(request, 'paciente.html', {'paciente':paciente})
            
        except Paciente.DoesNotExist():
            return render(request, 'paciente.html', {'paciente':paciente, 'error':True })
