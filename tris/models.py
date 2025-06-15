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
    
    def __str__(self):
        return self.user.username
