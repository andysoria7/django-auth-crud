from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Task(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField(blank=True)
    created = models.DateTimeField(auto_now_add=True) # Añade por defecto si nosotros no le pasamos este dato.
    datecompleted = models.DateTimeField(null=True, blank=True)
    important = models.BooleanField(default=False)
    user = models.ForeignKey(User, on_delete=models.CASCADE) # Relacionada con la tabla user / si se elimina el usuario se eliminan las tareas.
    
    def __str__(self):
        return self.title + '- by ' + self.user.username
        