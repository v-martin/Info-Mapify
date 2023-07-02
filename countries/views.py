from django.shortcuts import render
from countries.models import Country


def show_by_id(request):
    pk = request.GET.get('pk', 1)
    # if 1 > pk or pk > 193:
    #     pk = 1
    country = Country.objects.get(id=pk)
    context = {'name': country.name}
    return render(request, 'homepage.html', context)
