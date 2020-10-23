from django.urls import path
from . import views

from . import views

urlpatterns = [
    path('', views.index, name='homepage'),
    path('user_login/',views.user_login,name='user_login'),
]