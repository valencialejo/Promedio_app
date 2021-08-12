from django.shortcuts import render,redirect
from django.views.generic.list import ListView
from Promedio.models import Estudiante

# Create your views here.

def Home(request):
    estudiantes_listados=Estudiante.objects.all()
    data ={
        'titulo':'Notas',
        'Estudiantes':estudiantes_listados
    }
    return render(request,"menu.html")

class EstudiantesListView(ListView):
    model=Estudiante
    template_name='menu.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["titulo"] = 'Gestor de promedios' 
        return context  
    
def eliminar_estudiante(request,id):
    curso=Estudiante.objects.get(id=id)
    curso.delete()

    return redirect('/')

def registrar_estudiante(request):
    nombre=request.POST['nombre']
    parcial1=request.POST['parcial1']
    parcial2=request.POST['parcial2']
    parcial3=request.POST['parcial3']
    promedio=round((float(parcial1)+float(parcial2)+float(parcial3))/3,2) 
    curso=Estudiante.objects.create(nombre=nombre,parcial1=parcial1,parcial2=parcial2,parcial3=parcial3,promedio=promedio)

    return redirect('/')