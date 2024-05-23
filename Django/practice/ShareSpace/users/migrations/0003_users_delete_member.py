# Generated by Django 5.0.6 on 2024-05-23 10:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0002_member_joined_date_member_phone'),
    ]

    operations = [
        migrations.CreateModel(
            name='Users',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('firstname', models.CharField(max_length=255)),
                ('lastname', models.CharField(max_length=255)),
                ('phone', models.IntegerField(null=True)),
                ('email', models.CharField(max_length=255)),
                ('joined_date', models.DateField(null=True)),
            ],
        ),
        migrations.DeleteModel(
            name='Member',
        ),
    ]
