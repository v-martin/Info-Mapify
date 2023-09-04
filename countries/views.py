from django.shortcuts import render, redirect
from services.infrastructure.country_orm import get_country_by_code, get_country_by_name, get_countries


def countries_list(request):
    """
    Display an list of CountryEntities.

    **Context**

    ``list``
        A list of `country_orm.CountryEntity`.

    **Template:**

    :template:`countries/templates/home.html`

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
    return render(request, 'home.html', context)


def country_by_code(request, code):
    """
    Display a CountryEntity by it`s code.

    **Context**

    ``country``
        An instance of :CountryEntity:`country_orm.CountryEntity`.

    **Template:**

    :template:`countries/templates/country.html`

    """
    country = get_country_by_code(code)
    context = {'name': country.name, 'gdp': country.curr_gdp, 'country_code': country.code}
    return render(request, 'country.html', context)

