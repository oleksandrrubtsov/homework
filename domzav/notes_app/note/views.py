
from django.shortcuts import get_object_or_404, render
from django.http import HttpResponse, HttpResponseRedirect
from django.template import loader
from .forms import CreateNewList
from .models import Choice, Question
from django.urls import reverse



def index(request):
    template = loader.get_template("note.html")
    return HttpResponse(template.render())


def create(response):
    return render(response, "create.html", {})

def primary(response):
    return render(response,"primary.html")

def secondary(response):
    return render(response, "secondary.html")

def success(response):
    return render(response,"success.html")

def danger (response):
    return render(response,"danger.html")

def warning (response):
    return render(response, "warning.html")

def info (response):
    return render(response, "info.html")

def light (response):
    return render(response,"light.html")


    


   







