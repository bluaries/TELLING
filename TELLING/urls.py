from django.urls import path
from . import views

app_name = 'TELLING'
urlpatterns = [
    path('', views.IndexView.as_view(), name='homepage'),
    path('create/', views.create_story, name='create_story'),
]