from django.contrib import admin
from .models import Task # Importo mi modelo Task desde models.py

class TaskAdmin(admin.ModelAdmin): # Para ver los campos de solo lectura en el administrador.
    readonly_fields = ('created', )
    
# Register your models here.
admin.site.register(Task, TaskAdmin) # Para que mi tabla tenga acceso al panel del administrador de django.

