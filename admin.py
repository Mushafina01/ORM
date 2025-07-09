## Review System
from django.contrib import admin
from .models import Product, Review

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')
    search_fields = ('name',)

@admin.register(Review)
class ReviewAdmin(admin.ModelAdmin):
    list_display = ('id', 'user', 'product', 'rating', 'created_at')
    search_fields = ('user__username', 'product__name')

---

## Movie-Actor Relationship 
from django.contrib import admin
from .models import Movie, Actor

@admin.register(Actor)
class ActorAdmin(admin.ModelAdmin):
    list_display = ('name', 'birth_date')
    search_fields = ('name',)

@admin.register(Movie)
class MovieAdmin(admin.ModelAdmin):
    list_display = ('title', 'release_date')
    search_fields = ('title',)
    filter_horizontal = ('actors',)  
