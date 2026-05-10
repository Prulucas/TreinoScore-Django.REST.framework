from django.urls import path
from . import views

app_name = 'users'

urlpatterns = [
    path('profile', views.user_dashbord, name='profile'),
]
