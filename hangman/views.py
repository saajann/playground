from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import HangmanGame, HangmanWord
import random
from django.template import loader
from django.http import HttpResponse
from .forms import LetterForm

# Create your views here.

@login_required
def hangman(request):
    games = HangmanGame.objects.filter(user=request.user, is_over=True)
    wins = games.count()
    template = loader.get_template('hangman.html')
    context = {
        'wins': wins,
    }
    return HttpResponse(template.render(context, request))

def finished(request):
    pass

@login_required
def new_game(request):
    word = random.choice(HangmanWord.objects.all())
    game = HangmanGame.objects.create(user=request.user, word=word)
    return redirect('play_game', game_id=game.id)

@login_required
def play_game(request, game_id):
    game = get_object_or_404(HangmanGame, id=game_id, user=request.user)
    form = LetterForm()

    if request.method == 'POST' and not game.is_over:
        form = LetterForm(request.POST)
        if form.is_valid():
            letter = form.cleaned_data['letter']
            if letter not in game.guessed_letters:
                game.guessed_letters += letter
                if letter not in game.word.text:
                    game.remaining_attempts -= 1

                if all(c in game.guessed_letters for c in game.word.text):
                    game.is_over = True
                    game.won = True
                elif game.remaining_attempts <= 0:
                    game.is_over = True
                    game.won = False
                game.save()

    display_word = ' '.join([c if c in game.guessed_letters else '_' for c in game.word.text])

    return render(request, 'game_hangman.html', {
        'game': game,
        'display_word': display_word,
        'letters': 'abcdefghijklmnopqrstuvwxyz',
        'form': form
    })