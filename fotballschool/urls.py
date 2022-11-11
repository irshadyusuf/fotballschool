from django.urls import path
from . import views

app_name ='fotballschool'


urlpatterns = [
     path('login', views.login_fun, name='log'),
     path('club', views.club_fun, name='clu'),
     path('ticket', views.ticket_fun, name='tic'),
     path('scedule', views.scedule_fun, name='sce'),
     path('young', views.young_fun, name='you'),


]
