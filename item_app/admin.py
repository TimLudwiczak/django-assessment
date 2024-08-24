from django.contrib import admin
from .models import Item

@admin.register(Item)
class ItemAdmin(admin.ModelAdmin):
    list_display = ('name', 'price')  # Customize as needed
    search_fields = ('name', 'description')  # Optional: add search functionality
    list_filter = ('price',)  # Optional: add filters for price
