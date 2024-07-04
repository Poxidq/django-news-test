from django.contrib import admin
from .models import Favorite


# class FavoriteAdmin(admin.ModelAdmin):
#     list_display = ("title", "user", "published_at", "url")
#     search_fields = ("title", "user__username")
#     list_filter = ("user", "published_at")
#     readonly_fields = ("title", "user", "description", "url", "published_at")


admin.site.register(Favorite)
