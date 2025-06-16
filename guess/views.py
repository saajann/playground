from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from django.template import loader
from django.contrib.auth.decorators import login_required
from .models import GuessGame
from .forms import GuessForm
import random

# Create your views here.

@login_required
def guess(request):
    games = GuessGame.objects.filter(user=request.user, is_over=True)
    attempts = sum(game.attempts for game in games)
    wins = games.count()
    template = loader.get_template('guess.html')
    context = {
        'wins': wins,
        'attempts': attempts,
    }
    return HttpResponse(template.render(context, request))

def finished(request):
    pass

@login_required
def new_game(request):
    number = random.randint(1, 100)
    game = GuessGame.objects.create(number=number, user=request.user)
    return redirect('play_game_guess', game_id=game.id)

@login_required
def play_game(request, game_id):
    game = get_object_or_404(GuessGame, id=game_id, user=request.user)
    result = None

    if request.method == 'POST' and not game.is_over:
        number = int(request.POST.get('numero'))

        if number is not None and 1 <= number <= 100:
            game.attempts += 1
            if number == game.number:
                game.is_over = True
                game.save()
                result = 'correct'
            elif number < game.number:
                game.save()
                result = 0
            else:
                game.save()
                result = 1

    context = {
        'game': game,
        'result': result,
    }
    return render(request, 'game-guess.html', context)
