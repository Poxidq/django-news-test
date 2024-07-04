from django.shortcuts import redirect, render
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
    news = get_articles(category="django", pageSize=10)
    return render(request, "index.html", {"news_items": news})


# Возвращает понравившиеся новости
def favorites_view(request):
    items = Favorite.objects.all()
    return render(request, "favorite_items.html", {"favorite_items": items})


def add_fovorite(request):
    if request.method == "POST":
        ...

    return redirect("/")
