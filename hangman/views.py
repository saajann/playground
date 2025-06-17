from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import HangmanGame, HangmanWord
import random
from django.template import loader
from django.http import HttpResponse
from .forms import LetterForm, AddWordForm, EditWordForm, CSVUploadForm

import csv
from io import TextIOWrapper
from django.contrib import messages
import re

# Create your views here.

@login_required
def hangman(request):
    games = HangmanGame.objects.filter(user=request.user, is_over=True)
    wins = games.filter(won=True).count()
    losses = games.filter(won=False).count()
    template = loader.get_template('hangman.html')
    context = {
        'wins': wins,
        'losses': losses
    }
    return HttpResponse(template.render(context, request))

@login_required
def hangman_finished(request, id):
    
    game = get_object_or_404(HangmanGame, id=id, user=request.user)
    
    template = loader.get_template('hangman_finished.html')
    context = {
        'game': game
    }
    return HttpResponse(template.render(context, request))

@login_required
def new_game(request):
    word = random.choice(HangmanWord.objects.all())
    game = HangmanGame.objects.create(user=request.user, word=word)
    return redirect('play_game_hangman', game_id=game.id)

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

@login_required
def add_word(request):
    words = HangmanWord.objects.all()
    if request.method == 'POST':
        form = AddWordForm(request.POST)
        if form.is_valid():
            word = form.save(commit=False)
            word.save()
            return redirect('/hangman/words/')
    else:
        form = AddWordForm()
    template = loader.get_template('words.html')
    context = {
        'form': form,
        'words': words
    }
    return HttpResponse(template.render(context, request))

@login_required
def delete_word(request, id):
    word = get_object_or_404(HangmanWord, id=id)
    word.delete()
    return redirect('/hangman/words/')

@login_required
def edit_word(request, id):
    word = get_object_or_404(HangmanWord, id=id)
    if request.method == 'POST':
        form = EditWordForm(request.POST, instance=word)
        if form.is_valid():
            form.save()
            return redirect('/hangman/words/')
    else:
        form = EditWordForm(instance=word)
    return render(request, 'words_edit.html', {'form': form, 'word': word})

@login_required
def delete_words(request):
    word_ids = request.POST.getlist("word_ids")
    if word_ids:
        HangmanWord.objects.filter(id__in=word_ids).delete()
    return redirect("/hangman/words/")

@login_required
def upload_csv(request):
    if request.method == 'POST':
        form = CSVUploadForm(request.POST, request.FILES)
        if form.is_valid():
            file = form.cleaned_data['file']
            decoded_file = TextIOWrapper(file, encoding='utf-8')
            reader = csv.reader(decoded_file)
            for row in reader:
                if row:
                    word = ''.join([c for c in row[0].strip() if c.isalpha()])
                    if word:
                        HangmanWord.objects.get_or_create(text=word.lower())
            messages.success(request, 'File uploaded!')
            return redirect('upload_csv')
    else:
        form = CSVUploadForm()
    return render(request, 'upload.html', {'form': form})