from django.db import models

# Create your models here.
class User(models.Model):
    firstname = models.CharField(max_length= 255)
    lastname = models.CharField(max_length=255)
    phone = models.IntegerField(null=True)
    email = models.CharField(max_length=255)
    joined_date = models.DateField(null=True)

    def __str__(self):
        return f"{self.firstname} {self.lastname}"

class Product(models.Model):
    name= models.CharField(max_length=255)
    category = models.CharField(max_length=255)
    description = models.TextField(null=True, blank=True)
    date_added = models.DateField(null=True)


    # one to many relationships
    users = models.ForeignKey(User, on_delete=models.CASCADE, null=True)


    def __str__(self):
        return self.name
