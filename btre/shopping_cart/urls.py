from django.urls import path
from . import views
# localhost:8000/cart/

urlpatterns = [
    path('', views.index, name = 'index'),
    path('view/', views.view, name = 'view')
]