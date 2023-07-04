from django.urls import path
from . import views


urlpatterns = [
    path('', views.show_by_id, name='show'),
    path('home', views.show_by_id, name='home'),
    path('sign-up', views.sign_up, name='sign_up'),
]
