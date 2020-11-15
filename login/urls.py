from django.urls import path
from login import views

app_name = "login"

urlpatterns = [
    path('register/',views.register,name='register'),
    path('',views.user_login,name='user_login'),
]
