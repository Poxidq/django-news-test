from django.urls import path
from . import views

urlpatterns = [
    path("", views.homepage_view),
    path("favorites", views.favorites_view, name="favorites"),
    path("add_favorite", views.add_fovorite, name="add"),
]
