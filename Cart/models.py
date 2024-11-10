from django.db import models
from django.contrib.auth import get_user_model
from Menu.models import Menu
User = get_user_model()

class Cart(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True, related_name="carts")
    session_id = models.CharField(max_length=255, null=True, blank=True)  # معرف الجلسة
    menu_item = models.ForeignKey(Menu, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)
    
    def total_price(self):
        return self.menu_item.price * self.quantity
    
    def __str__(self):
        if self.user:
            return f"{self.menu_item.name} - {self.user.email}"
        return f"{self.menu_item.name} - Session {self.session_id}"
    
    class Meta:
        unique_together = (("user", "menu_item"), ("session_id", "menu_item"))
