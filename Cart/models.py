from django.db import models
from django.contrib.auth import get_user_model
from Menu.models import Menu
User = get_user_model()

class Cart(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="carts")
    menu_item = models.ForeignKey(Menu, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)
    
    def total_price(self):
        return self.menu_item.price * self.quantity
    
    def __str__(self):
        return f"{self.menu_item.name} - {self.user.email}"
