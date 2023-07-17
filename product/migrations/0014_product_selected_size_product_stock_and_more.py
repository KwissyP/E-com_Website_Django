# Generated by Django 4.2.2 on 2023-07-15 21:37

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('product', '0013_remove_product_selected_size_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='selected_size',
            field=models.CharField(default='S', max_length=10),
        ),
        migrations.AddField(
            model_name='product',
            name='stock',
            field=models.JSONField(default=dict),
        ),
        migrations.AddField(
            model_name='product',
            name='wishlist_users',
            field=models.ManyToManyField(blank=True, related_name='wishlist_products', to=settings.AUTH_USER_MODEL),
        ),
        migrations.DeleteModel(
            name='Stock',
        ),
    ]
