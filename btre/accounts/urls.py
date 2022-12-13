from django.urls import path, include
from . import views


urlpatterns = [
    path('login', views.login, name = 'login'),
    path('logout', views.logout, name = 'logout'),
    path('register', views.register, name = 'register'),
    path('dashboard', views.dashboard, name = 'dashboard'),
]

