from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Campeon(models.Model):
    nombre = models.CharField(max_length=15)
    descripcion = models.CharField(max_length=25)
    dificultad = models.CharField(max_length=7)
    fecha_creacion = models.DateField(auto_now_add=True)
    publisher = models.ForeignKey(to=User, on_delete=models.CASCADE, related_name="publisher")
    imagen = models.ImageField(upload_to="campeones", null=True, blank=True)

    def __str__(self):
        return f"{self.id} - {self.nombre} - {self.descripcion} - {self.dificultad} - {self.fecha_creacion}"
    
class Profile(models.Model):
    user = models.OneToOneField(to=User, on_delete=models.CASCADE, related_name="profile")
    instagram = models.CharField(max_length=100)
    imagen = models.ImageField(upload_to="profile", null=True, blank=True)

class Mensaje(models.Model):
      mensaje = models.TextField(max_length=100)
      email = models.EmailField()
      destinatario = models.ForeignKey(to=User, on_delete=models.CASCADE, related_name="destinatario")