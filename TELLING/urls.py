from django.urls import path
from . import views

from . import views

app_name = 'TELLING'
urlpatterns = [
    path('', views.index, name='homepage'),
    path('create/', views.create_story, name='create_story'),
]