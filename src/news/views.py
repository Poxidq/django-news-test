from django.shortcuts import redirect, render

from news.forms import FavoriteForm
from .models import Favorite

import requests

API_KEY = "8b4c22d4730a4ab6a6c8adc267bfbefc"


def get_articles(category="all", lang="ru", pageSize=100):
    response = requests.get(
        f"https://newsapi.org/v2/everything?q={category}&language={lang}&pageSize={pageSize}&apiKey={API_KEY}"
    )
    data = response.json()
    if data["status"] != "ok":
        print("[!] Ошибка в получении новостей")
        return

    return data["articles"]


def homepage_view(request):
    news = get_articles(category="sport", pageSize=10)
    return render(request, "index.html", {"news_items": news})


# Возвращает понравившиеся новости
def favorites_view(request):
    items = Favorite.objects.all()
    return render(request, "favorite_items.html", {"favorite_items": items})


def add_favorite(request):
    if request.method == "POST":
        form = FavoriteForm(request.POST)
        if form.is_valid():
            favorite = form.save(commit=False)
            favorite.title = favorite.title or "No Title"
            favorite.description = favorite.description or "No Description"
            favorite.url = favorite.url or "http://example.com"
            favorite.published_at = favorite.published_at or None
            favorite.author = favorite.author or "Unknown Author"
            form.save()
            return redirect("favorites")
        print("ADD_FOVORITE")
        print(form.errors)
    return redirect("home")
