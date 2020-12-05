from django.urls import path
from . import views

app_name = 'TELLING'
urlpatterns = [
    path('', views.IndexView.as_view(), name='homepage'),
    path('create/story/', views.create_story, name='create_story'),
    path('create/story/chapter/', views.create_new_chapter, name='create_chapter'),
    path('stories/<int:pk>/', views.story_detail, name='detail')
]