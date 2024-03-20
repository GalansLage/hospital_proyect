from django.urls import path, include
# from rest_framework.documentation import include_docs_urls
# from rest_framework import routers
from mi_app import views
from django.contrib.auth import views as auth

# router = routers.DefaultRouter()
# router.register(r'citas', views.CitaView, 'citas')
# # router.register(r'medicos', views.MedicoView, 'medicos')
# router.register(r'pacientes', views.PacienteView, 'pacientes')
# router.register(r'pruebas', views.PruebaMedicaView, 'pruebas')
# router.register(r'tratamientos', views.TratamientoView, 'tratamientos')

urlpatterns = [
    # path("api/v1/", include(router.urls)),
    # path('docs/', include_docs_urls(title="Tablas API")),
    path('', views.index_view, name='index'),
    path('login/', views.iniciar_sesion, name='login'),
    path('paciente/<int:pk>', views.paciente_view, name='paciente'),
    path('medico/<int:pk>', views.medico_view, name='medico'),
    path('logout', auth.LogoutView.as_view(template_name='index.html'), name='logout'),

    path('update_paciente/<int:pk>', views.update_paciente, name='update_paciente')
]