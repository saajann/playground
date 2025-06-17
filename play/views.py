from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from django.contrib.auth.decorators import login_required
from tris.models import TrisGame
from guess.models import GuessGame
from hangman.models import HangmanGame
from django.contrib.auth.models import User
from like.models import Like

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
    users = User.objects.all()
    tris_leaderboard = []
    guess_leaderboard = []
    hangman_leaderboard = []
    for user in users:
        tris_wins = TrisGame.objects.filter(user=user, winner='X').count()
        tris_leaderboard.append({'id': user.id, 'username': user.username, 'wins': tris_wins})
        guess_wins = GuessGame.objects.filter(user=user, is_over=True).count()
        guess_leaderboard.append({'id': user.id, 'username': user.username, 'wins': guess_wins})
        hangman_wins = HangmanGame.objects.filter(user=user, is_over=True, won=True).count()
        hangman_leaderboard.append({'id': user.id, 'username': user.username, 'wins': hangman_wins})

    tris_leaderboard.sort(key=lambda x: x['wins'], reverse=True)
    guess_leaderboard.sort(key=lambda x: x['wins'], reverse=True)
    hangman_leaderboard.sort(key=lambda x: x['wins'], reverse=True)

    liked_users = Like.objects.filter(from_user=request.user).values_list('to_user_id', flat=True)

    template = loader.get_template('leaderboard.html')
    context = {
        'tris_leaderboard': tris_leaderboard,
        'guess_leaderboard': guess_leaderboard,
        'hangman_leaderboard': hangman_leaderboard,
        'liked_users': list(liked_users)
    }
    return HttpResponse(template.render(context, request))

@login_required
def profile(request):
    template = loader.get_template('profile.html')
    context = {
        
    }
    return HttpResponse(template.render(context,request))