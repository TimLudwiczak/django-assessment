from django.contrib import admin
from item_app.models import Item
from cart_app.models import Cart, CartItem  # Import Cart and CartItem from cart_app
from .models import Client  # Import Client from the current app

admin.site.register(Client)
admin.site.register(Item)
admin.site.register(Cart)
admin.site.register(CartItem)
