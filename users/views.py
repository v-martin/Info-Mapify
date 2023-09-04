from typing import Optional

from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import AuthenticationForm
from django.core.handlers.wsgi import WSGIRequest
from django.http import HttpRequest
from django.shortcuts import render, redirect
from users.forms import SignUpForm


def sign_up(request: HttpRequest) -> render:
    """
    Sign up for the :model:`django.contrib.auth.models.User`.

    **Context**

    ``form``
        An instance of SighUpForm, that validates username, email and password.

    **Template:**

    :template:`users/templates/sign_up.html`

    """
    if request.method != 'POST':
        form = SignUpForm()
        return render(request, 'sign_up.html', {'form': form})

    form = SignUpForm(request.POST)
    if form.is_valid():
        user = form.save()
        login(request, user)
        return redirect('/home')

    return redirect('/sign-up')


def sign_in(request: HttpRequest) -> render:
    """
    Sign in for the :model:`django.contrib.auth.models.User`.

    **Context**

    ``form``
        An instance of AuthenticationForm, that validates username and password.

    ``user``
        An instance of :model:`django.contrib.auth.models.User`, that matches the entered username and password.

    **Template:**

    :template:`users/templates/login.html`

    """
    if request.method != 'POST':
        form = AuthenticationForm()
        return render(request, 'login.html', {'form': form})

    username = request.POST['username']
    password = request.POST['password']
    user = authenticate(request, username=username, password=password)

    if user is not None:
        login(request, user)
        return redirect('/home')

    return redirect('/login')
