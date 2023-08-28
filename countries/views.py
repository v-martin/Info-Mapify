from django.contrib.auth.forms import AuthenticationForm
from django.shortcuts import render, redirect
from services.infrastructure.country_orm import get_country_by_code, get_country_by_name, get_countries
from .forms import SignUpForm
from django.contrib.auth import login, logout, authenticate


def countries_list(request):
    """
    Display an list of CountryEntities.

    **Context**

    ``list``
        A list of `country_orm.CountryEntity`.

    **Template:**

    :template:`countries/templates/countries/home.html`

    """
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
    """
    Display a CountryEntity by it`s code.

    **Context**

    ``country``
        An instance of :CountryEntity:`country_orm.CountryEntity`.

    **Template:**

    :template:`countries/templates/countries/country.html`

    """
    country = get_country_by_code(code)
    context = {'name': country.name, 'gdp': country.curr_gdp, 'country_code': country.code}
    return render(request, 'countries/country.html', context)


def sign_up(request):
    """
    Sign up for the :model:`django.contrib.auth.models.User`.

    **Context**

    ``form``
        An instance of SighUpForm, that validates username, email and password.

    **Template:**

    :template:`countries/templates/registration/sign_up.html`

    """
    if request.method != 'POST':
        form = SignUpForm()
        return render(request, 'registration/sign_up.html', {'form': form})

    form = SignUpForm(request.POST)
    if form.is_valid():
        user = form.save()
        login(request, user)
        return redirect('/home')

    return redirect('/sign-up')


def sign_in(request):
    """
    Sign in for the :model:`django.contrib.auth.models.User`.

    **Context**

    ``form``
        An instance of AuthenticationForm, that validates username and password.

    ``user``
        An instance of :model:`django.contrib.auth.models.User`, that matches the entered username and password.

    **Template:**

    :template:`countries/templates/registration/login.html`

    """
    if request.method != 'POST':
        form = AuthenticationForm()
        return render(request, 'registration/login.html', {'form': form})

    username = request.POST['username']
    password = request.POST['password']
    user = authenticate(request, username=username, password=password)

    if user is not None:
        login(request, user)
        return redirect('/home')

    return redirect('/login')
