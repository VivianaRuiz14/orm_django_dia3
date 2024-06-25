from django.db import models

# Create your models here.

class tarea(models.Model):
    descripcion = models.TextField(default='', unique=True)
    eliminada = models.BooleanField(default=False)
    
class subtarea(models.Model):
    descripcion = models.TextField(default='')
    eliminada = models.BooleanField(default=False)
    tarea = models.ForeignKey(tarea, related_name='subtareas', on_delete= models.CASCADE)
    