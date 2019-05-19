from django.conf.urls import url
from django.urls import path
from . import views

app_name = 'final'
urlpatterns = [
    url(r'^$', views.home, name='homefinal'),
    path('cooperamos', views.cooperamos, name='cooperamosfinal'),
    path('hacemos', views.hacemos, name='hacmeosfinal'),
    path('somos', views.somos, name='somosfinal'),
]