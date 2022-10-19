from django.urls import path
from . import views
# 127.0.0.1:8000/listings/search
urlpatterns = [
    path('', views.index, name = "listings"),
    path('search', views.search, name = "search"),
    path('<int:listing_id>', views.listing, name = "listing"),
]
