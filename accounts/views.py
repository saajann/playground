from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.template import loader
from django.contrib.auth.models import User
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.decorators import login_required
from .forms import UserRegistrationForm, UserLoginForm

# Create your views here.

def user_registration(request):
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.set_password(form.cleaned_data['password'])
            user.save()
            #return redirect('/login/')
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(username=username, password=password)
            if user:
                login(request, user)
                return redirect('/play/')
    else:
        form = UserRegistrationForm()
    template = loader.get_template('registration.html')
    context = {
        'form': form
    }
    return HttpResponse(template.render(context, request))

def user_login(request):
    if request.method == 'POST':
        form = UserLoginForm(request.POST)
        if form.is_valid():
            username = request.POST['username']
            password = request.POST['password']
            user = authenticate(username=username, password=password)
            if user:
                login(request, user)
                return redirect('/play/')
    else:
        form = UserLoginForm()
    template = loader.get_template('login.html')
    context = {
        'form': form
    }
    return HttpResponse(template.render(context, request))

def user_logout(request):
    logout(request)
    return redirect('/')

def home(request):
    if request.user.is_authenticated:
        return redirect('/play/')
    template = loader.get_template('home.html')
    context = {

    }
    return HttpResponse(template.render(context,request)) 