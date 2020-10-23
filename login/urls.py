from django.urls import path
from login import views

app_name = "login"

urlpatterns = [
    path('user_login/',views.user_login,name='user_login'),
]
