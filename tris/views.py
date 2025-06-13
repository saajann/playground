from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader

# Create your views here.

def tris(request):
    template = loader.get_template('tris.html')
    context = {

    }
    return HttpResponse(template.render(context,request)) 