# Generated by Django 4.2.2 on 2023-07-15 18:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0008_remove_product_stockl_remove_product_stockm_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='product',
            name='tailleL',
        ),
        migrations.RemoveField(
            model_name='product',
            name='tailleM',
        ),
        migrations.RemoveField(
            model_name='product',
            name='tailleS',
        ),
        migrations.RemoveField(
            model_name='product',
            name='tailleXL',
        ),
        migrations.RemoveField(
            model_name='product',
            name='tailleXXL',
        ),
        migrations.AddField(
            model_name='product',
            name='stock',
            field=models.JSONField(default=dict),
        ),
    ]
