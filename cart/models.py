from django.db import models
from user.models import User
from product.models import Product

class Cart(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    products = models.ManyToManyField(Product, through='CartItem')

    def __str__(self):
        return f"Cart for {self.user.username}"

class CartItem(models.Model):
    cart = models.ForeignKey(Cart, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=0)
    size = models.CharField(max_length=10, default='S')
    
    def update_subtotal(self):
        self.subtotal = self.quantity * self.product.price
        self.save()

    def __str__(self):
        return f"{self.product.name} ({self.quantity})"