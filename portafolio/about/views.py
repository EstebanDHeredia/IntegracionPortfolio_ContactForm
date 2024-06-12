from django.shortcuts import render
from .models import Formacion, Skill

# Create your views here.
def about(request):
    formaciones = Formacion.objects.all()
    skills = Skill.objects.all()
    return render(request, "about/about.html", { "formaciones" : formaciones,
                                                "skills" : skills})