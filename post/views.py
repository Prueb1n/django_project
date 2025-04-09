from django.shortcuts import render
from django.views.generic import TemplateView
# Create your views here.

def hola_mundo(request):
    return render(request,"defHome.html")

class HolaMundoView(TemplateView):

    template_name="classHome.html"
