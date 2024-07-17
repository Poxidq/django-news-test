from django.urls import path
from . import views

urlpatterns = [
    path("", views.homepage_view, name="home"),
    path("favorites", views.favorites_view, name="favorites"),
    path("add_favorite", views.add_favorite, name="add_favorite"),
]
