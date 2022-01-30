from django.db import models

# Create your models here.

class Category(models.Model):
    name = models.CharField(max_length=1024)
    def __str__(self):
        return f"({self.pk}) {name}"

class Product(models.Model):
    name = models.CharField(max_length=1024)
    description = models.TextField()
    def __str__(self):
        return self.name

class CategoryLink(models.Model):
    product = models.ForeignKey(Product)
    category = models.ForeignKey(Category)

