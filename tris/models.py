from django.db import models
from django.contrib.auth.models import User
import json

# Create your models here.

class TrisGame(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    square_1_1 = models.CharField(max_length=1, blank=True, default='')
    square_1_2 = models.CharField(max_length=1, blank=True, default='')
    square_1_3 = models.CharField(max_length=1, blank=True, default='')
    square_2_1 = models.CharField(max_length=1, blank=True, default='')
    square_2_2 = models.CharField(max_length=1, blank=True, default='')
    square_2_3 = models.CharField(max_length=1, blank=True, default='')
    square_3_1 = models.CharField(max_length=1, blank=True, default='')
    square_3_2 = models.CharField(max_length=1, blank=True, default='')
    square_3_3 = models.CharField(max_length=1, blank=True, default='')
    is_over = models.BooleanField(default=False)
    winner = models.CharField(max_length=10, choices=[('X', 'X'), ('O', 'O'), ('Draw', 'Draw')], blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def get_board(self):
        return json.loads(self.board)

    def set_board(self, board_data):
        self.board = json.dumps(board_data)

    def current_turn(self):
        board = self.get_board()
        x = sum(row.count("X") for row in board)
        o = sum(row.count("O") for row in board)
        return "X" if x <= o else "O"
    
    def __str__(self):
        return self.user.username
