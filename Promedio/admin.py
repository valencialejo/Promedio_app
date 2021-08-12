from django.contrib import admin
from .models import Estudiante

# Register your models here.
@admin.register(Estudiante)
class EstudianteAdmin(admin.ModelAdmin):
    list_display=('id','nombre','parcial1','parcial2','parcial3','promedio')
    list_editable = ('nombre',)
    

    fieldsets = (
        (None, {
            'fields': ('nombre','parcial1','parcial2','parcial3')
        }),
    )