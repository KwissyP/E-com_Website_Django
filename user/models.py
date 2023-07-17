from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.

class Role(models.Model):
    ADMIN = 'Admin'
    WEB = 'Web'
    STOCK = 'Stock'
    MEMBER = 'Member'

    ROLE_CHOICES = [
        (ADMIN, 'Admin'),
        (WEB, 'Web'),
        (STOCK, 'Stock'),
        (MEMBER, 'Member'),
    ]

    value = models.CharField(max_length=50, choices=ROLE_CHOICES)

    def __str__(self):
        return self.get_value_display()

class User(AbstractUser):
    role = models.ForeignKey(Role, on_delete=models.CASCADE, blank=True, null=True)
    img_url = models.CharField(max_length=250)
    is_subscribed = models.BooleanField(default=False)
    produits_wishlist = models.ManyToManyField('product.Product', related_name='wishlists', blank=True)

    def __str__(self):
        return self.username