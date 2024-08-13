from django.db import models
from django.contrib.auth.models import User
from item_app.models import Item  # Import the Item model

class Cart(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)  # Link cart to a user
    created_at = models.DateTimeField(auto_now_add=True)  # Track when the cart was created

    def __str__(self):
        return f'Cart for {self.user.username}'

class CartItem(models.Model):
    cart = models.ForeignKey(Cart, related_name='items', on_delete=models.CASCADE)  # Link cart item to a cart
    item = models.ForeignKey(Item, on_delete=models.CASCADE)  # Link cart item to an item
    quantity = models.PositiveIntegerField(default=1)  # Track quantity of the item

    def __str__(self):
        return f'{self.item.name} (x{self.quantity})'
