from django.contrib import admin
from .models import (
    Category,
    City,
    Advert
)

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    """Admin class template for the 'Category' models"""
    pass

@admin.register(City)
class CityAdmin(admin.ModelAdmin):
    """Admin class template for the 'City' models"""
    pass

@admin.register(Advert)
class AdvertAdmin(admin.ModelAdmin):
    """Admin class template for the 'Advert' models"""
    pass

