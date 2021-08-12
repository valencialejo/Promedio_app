from django.urls import path
from Promedio.views import *

urlpatterns = [
    path('',EstudiantesListView.as_view(),name='gestion_estudiantes'),
    path('registrarEstudiante/',registrar_estudiante),
    path('eliminarEstudiante/<int:id>', eliminar_estudiante)
]