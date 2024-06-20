from django.urls import path
from . import views

#
urlpatterns = [
    path("", views.homepage_view),
    # path("news_homepage2", views.homepage_view),
]
