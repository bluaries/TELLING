from django.urls import path

from . import views

app_name = 'TELLING'
urlpatterns = [
    path('', views.index, name='homepage'),
]