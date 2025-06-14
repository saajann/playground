from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from django.contrib.auth.decorators import login_required
from tris.models import TrisGame

# Create your views here.

@login_required
def play(request):
    template = loader.get_template('play.html')
    context = {

    }
    return HttpResponse(template.render(context,request)) 

@login_required
def past_games(request):
    template = loader.get_template('past_games.html')
    tris_past_games = TrisGame.objects.filter(user=request.user)
    context = {
        'tris_past_games': tris_past_games
    }
    return HttpResponse(template.render(context,request))

@login_required
def leaderboard(request):
    template = loader.get_template('leaderboard.html')
    context = {
        
    }
    return HttpResponse(template.render(context,request))

@login_required
def stats(request):
    template = loader.get_template('stats.html')
    context = {
        
    }
    return HttpResponse(template.render(context,request))