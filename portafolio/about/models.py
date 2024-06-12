from django.db import models

# Create your models here.
class Formacion(models.Model):
    name = models.CharField(max_length=150, verbose_name="Nombre")
    obtained_title = models.CharField(max_length=100, verbose_name="Título Obtenido")
    description = models.TextField(verbose_name="Descripción")
    obtained_date = models.DateField(verbose_name="Fecha de obtención")

    def __str__(self) -> str:
        return self.name
    
    class Meta:
        verbose_name = "Formación"
        verbose_name_plural = "Cursos"
        ordering = ['-obtained_date']

class Skill(models.Model):
    name = models.CharField(max_length=20, verbose_name="Conocimiento")
    image = models.ImageField(upload_to="skills", verbose_name="Imagen")
    
    def __str__(self) -> str:
        return self.name
    
    class Meta:
        verbose_name = "Conocimiento"
        verbose_name_plural = "Conocimientos"
