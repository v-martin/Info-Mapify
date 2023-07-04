from django.shortcuts import render, redirect
from .models import Country
from .forms import SignUpForm
from django.contrib.auth import login, logout, authenticate


def show_by_id(request):
    pk = request.GET.get('pk', 1)
    # if 1 > pk or pk > 193:
    #     pk = 1
    country = Country.objects.get(id=pk)
    context = {'name': country.name}
    return render(request, 'countries/home.html', context)


def sign_up(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = form.save()
            user.save()
            login(request, user)
            return redirect('/home')
    else:
        form = SignUpForm()

    return render(request, 'registration/sign_up.html', {'form': form})
