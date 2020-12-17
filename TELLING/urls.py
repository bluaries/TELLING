from django.urls import path
from . import views

app_name = 'TELLING'
urlpatterns = [
    path('', views.index, name='homepage'),
    path('create/story/', views.create_story, name='create_story'),
    path('create/story/<int:pk>/chapter/', views.create_new_chapter, name='create_chapter'),
    path('story/<int:pk>/', views.story_detail, name='detail'),
    path('mystory/', views.show_user_story, name='show_story'),
    path('story/edit/<int:pk>/', views.edit_story, name='edit_story'),
    path('story/chapter/<int:pk>/', views.chapter_detail, name='chapter'),
    path('chapter/edit/<int:pk>/', views.edit_chapter, name='edit_chapter'),
     path('story/delete/<int:pk>/', views.del_story, name='del_story'),

   
]