from django.shortcuts import render
from countries.models import Country


def show_by_id(request):
    pk = request.GET.get('pk', '')
    name = Country.objects.filter(pk=pk)
    context = {'name': name}
    return render(request, 'mainpage.html', context)
