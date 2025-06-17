from django.contrib.auth.decorators import login_required
from django.http import JsonResponse, HttpResponseBadRequest
from django.shortcuts import get_object_or_404, redirect
from .models import Like
from django.contrib.auth.models import User
from django.db import IntegrityError

@login_required
def like_user(request, id):
    to_user = get_object_or_404(User, id=id)
    Like.objects.create(from_user=request.user, to_user=to_user)
    return redirect('/play/leaderboard/')

@login_required
def remove_like_user(request, id):
    to_user = get_object_or_404(User, id=id)
    Like.objects.filter(from_user=request.user, to_user=to_user).delete()
    return redirect('/play/leaderboard/')