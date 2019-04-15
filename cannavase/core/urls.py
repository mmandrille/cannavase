from django.conf.urls import url
from django.urls import path
from . import views

app_name = 'corecannava'
urlpatterns = [
    url(r'^$', views.home, name='home'),

    path('contacto/', views.contacto, name='contacto'),
]