# Generated by Django 4.2.2 on 2023-07-18 13:30

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('contact', '0002_contactmessage'),
    ]

    operations = [
        migrations.DeleteModel(
            name='ContactMessage',
        ),
    ]
