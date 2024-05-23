# Generated by Django 5.0.6 on 2024-05-23 11:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0003_users_delete_member'),
    ]

    operations = [
        migrations.CreateModel(
            name='Products',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('category', models.CharField(max_length=255)),
                ('date_added', models.DateField(null=True)),
            ],
        ),
    ]