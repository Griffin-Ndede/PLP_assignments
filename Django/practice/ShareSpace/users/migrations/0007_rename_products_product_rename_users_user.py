# Generated by Django 5.0.6 on 2024-05-23 11:39

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0006_products_description'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Products',
            new_name='Product',
        ),
        migrations.RenameModel(
            old_name='Users',
            new_name='User',
        ),
    ]