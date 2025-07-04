from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from django.template import loader
from django.contrib.auth.decorators import login_required
from .models import TrisGame
import random
from .forms import MoveForm

# Create your views here.

@login_required
def tris(request):
    wins = TrisGame.objects.filter(user=request.user, winner='X').count()
    losses = TrisGame.objects.filter(user=request.user, winner='O').count()
    draws = TrisGame.objects.filter(user=request.user, winner='Draw').count()
    template = loader.get_template('tris.html')
    context = {
        'wins': wins,
        'losses': losses,
        'draws': draws,
    }
    return HttpResponse(template.render(context,request)) 

@login_required
def tris_finished(request, id):
    
    game = get_object_or_404(TrisGame, id=id, user=request.user)
    
    template = loader.get_template('tris_finished.html')
    context = {
        'game': game
    }
    return HttpResponse(template.render(context, request))

def check_winner(board):
    columns = [list(col) for col in zip(*board)]
    lines = board + columns + [
        [board[i][i] for i in range(3)],
        [board[i][2 - i] for i in range(3)]
    ]
    for line in lines:
        if line == ['X'] * 3:
            return 'X'
        elif line == ['O'] * 3:
            return 'O'
    if all(cell in ['X', 'O'] for row in board for cell in row):
        return 'Draw'
    return None

@login_required
def new_game_ai(request):
    game = TrisGame.objects.create(user=request.user)
    return redirect('play_game_ai', game_id=game.id)

@login_required
def play_game_ai(request, game_id):
    game = get_object_or_404(TrisGame, id=game_id, user=request.user)
    form = MoveForm()

    board = [
        [game.square_1_1, game.square_1_2, game.square_1_3],
        [game.square_2_1, game.square_2_2, game.square_2_3],
        [game.square_3_1, game.square_3_2, game.square_3_3],
    ]

    if request.method == 'POST' and not game.is_over:
        form = MoveForm(request.POST)
        if form.is_valid():
            row, col = form.cleaned_data['row'] - 1, form.cleaned_data['col'] - 1
            if board[row][col] == '':
                board[row][col] = 'X'

                winner = check_winner(board)
                if winner:
                    game.is_over = True
                    game.winner = winner
                else:
                    empty = [(i, j) for i in range(3) for j in range(3) if board[i][j] == '']
                    if empty:
                        i, j = random.choice(empty)
                        board[i][j] = 'O'
                        winner = check_winner(board)
                        if winner:
                            game.is_over = True
                            game.winner = winner

                game.square_1_1, game.square_1_2, game.square_1_3 = board[0]
                game.square_2_1, game.square_2_2, game.square_2_3 = board[1]
                game.square_3_1, game.square_3_2, game.square_3_3 = board[2]
                game.save()
                return redirect('play_game_ai', game_id=game.id)
            
    flat_board = []
    for i in range(3):
        row = []
        for j in range(3):
            row.append({
                'value': board[i][j],
                'row': i + 1,
                'col': j + 1,
            })
        flat_board.append(row)

    context = {
        'game': game,
        'board': flat_board,
        'form': form,
    }
    return render(request, 'game-ai.html', context)

@login_required
def new_game_player(request):
    game = TrisGame.objects.create(user=request.user)
    return redirect('play_game_player', game_id=game.id)

@login_required
def play_game_player(request, game_id):
    game = get_object_or_404(TrisGame, id=game_id, user=request.user)
    form = MoveForm()

    board = [
        [game.square_1_1, game.square_1_2, game.square_1_3],
        [game.square_2_1, game.square_2_2, game.square_2_3],
        [game.square_3_1, game.square_3_2, game.square_3_3],
    ]

    x_count = sum(row.count('X') for row in board)
    o_count = sum(row.count('O') for row in board)
    temp = 'X' if x_count == o_count else 'O'

    if request.method == 'POST' and not game.is_over:
        form = MoveForm(request.POST)
        if form.is_valid():
            row, col = form.cleaned_data['row'] - 1, form.cleaned_data['col'] - 1
            if board[row][col] == '':
                board[row][col] = temp

                winner = check_winner(board)
                if winner:
                    game.is_over = True
                    game.winner = winner

                game.square_1_1, game.square_1_2, game.square_1_3 = board[0]
                game.square_2_1, game.square_2_2, game.square_2_3 = board[1]
                game.square_3_1, game.square_3_2, game.square_3_3 = board[2]
                game.save()
                return redirect('play_game_player', game_id=game.id)
            
    flat_board = []
    for i in range(3):
        row = []
        for j in range(3):
            row.append({
                'value': board[i][j],
                'row': i + 1,
                'col': j + 1,
            })
        flat_board.append(row)

    context = {
        'game': game,
        'board': flat_board,
        'form': form,
    }
    return render(request, 'game-player.html', context)
