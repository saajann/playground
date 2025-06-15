from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class HangmanWord(models.Model):
    text = models.CharField(max_length=50, unique=True)

    def __str__(self):
        return self.text

class HangmanGame(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    word = models.ForeignKey(HangmanWord, on_delete=models.CASCADE)
    guessed_letters = models.CharField(max_length=100, default="")
    remaining_attempts = models.IntegerField(default=6)
    is_over = models.BooleanField(default=False)
    won = models.BooleanField(null=True)