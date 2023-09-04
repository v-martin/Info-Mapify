from django.urls import path
from . import views


urlpatterns = [
    path('', views.countries_list, name='home'),
    path('home', views.countries_list, name='home'),
    path('country/<str:code>', views.country_by_code, name='country'),
]
