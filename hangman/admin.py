from django.contrib import admin
from .models import HangmanGame, HangmanWord

# Register your models here.

admin.site.register(HangmanGame)
admin.site.register(HangmanWord)