from django.utils import timezone
from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator
from django.db.models import JSONField
from user.models import User
from django.contrib.auth import get_user_model

class Category(models.Model):
    value = models.CharField(max_length=50, unique=True)
    
    def __str__(self):
        return self.value


class Product(models.Model):
    img1 = models.CharField(max_length=1000)
    img2 = models.CharField(max_length=1000)
    img3 = models.CharField(max_length=1000)
    description = models.TextField(max_length=300, null=True, blank=True)
    name = models.CharField(max_length=50)
    category = models.ForeignKey(Category, null=True, blank=True, on_delete=models.SET_NULL)
    price = models.PositiveIntegerField()
    promo = models.PositiveIntegerField(validators=[MaxValueValidator(100), MinValueValidator(0)])
    stock = JSONField(default=dict)
    selected_size = models.CharField(max_length=10, default='S')
    
    def get_stock_quantity(self, size):
        return self.stock.get(size, 0)

    def __str__(self):
        return self.name

class Note(models.Model):
    author = models.ForeignKey(User, null=True, blank=True, on_delete=models.CASCADE)
    anonymous_author = models.ForeignKey('AnonymousUser', null=True, blank=True, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    titre = models.CharField(max_length=50)
    text = models.TextField(max_length=300, default='valeur_par_défaut')
    created_at = models.DateTimeField(default=timezone.now)


class AnonymousUser(models.Model):
    name = models.CharField(max_length=50)
    email = models.EmailField()

