from django.contrib.auth.forms import AuthenticationForm
from django.shortcuts import render, redirect
from services.infrastructure.country_orm import get_country_by_code, get_country_by_name, get_countries
from .forms import SignUpForm
from django.contrib.auth import login, logout, authenticate


def countries_list(request):
    if request.GET.get('name'):
        try:
            country = get_country_by_name(request.GET.get('name'))
            return redirect(f'/country/{country.code.lower()}')
        except AttributeError:
            return redirect('/home')
    countries = get_countries()
    context_list = [(country.name, country.curr_gdp, country.code) for country in countries]
    context = {'list': context_list}
    return render(request, 'countries/home.html', context)


def country_by_code(request, code):
    country = get_country_by_code(code)
    context = {'name': country.name, 'gdp': country.curr_gdp, 'country_code': country.code}
    return render(request, 'countries/country.html', context)


def sign_up(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('/home')
        else:
            return redirect('/sign_up')
    else:
        form = SignUpForm()

    return render(request, 'registration/sign_up.html', {'form': form})


def sign_in(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('/home')
        else:
            return redirect('/login')
    else:
        form = AuthenticationForm()

    return render(request, 'registration/login.html', {'form': form})

