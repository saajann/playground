from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from django.contrib.auth.decorators import login_required
from .models import TrisGame
from django.shortcuts import get_object_or_404

# Create your views here.

@login_required
def tris(request):
    template = loader.get_template('tris.html')
    context = {

    }
    return HttpResponse(template.render(context,request)) 

@login_required
def game(request):
    template = loader.get_template('game.html')
    context = {

    }
    return HttpResponse(template.render(context,request)) 

@login_required
def finished(request, id):
    
    game = get_object_or_404(TrisGame, id=id, user=request.user)
    
    if not game.is_over:
        return HttpResponse("Game is not finished yet.")
    
    template = loader.get_template('finished.html')
    context = {
        'game': game
    }
    return HttpResponse(template.render(context, request))