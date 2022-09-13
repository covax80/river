from django.db import models

# Create your models here.
class Category(models.Model):
    class Meta:
        verbose_name = "Категория товара"
        verbose_name_plural = "Категории товаров"
        ordering = ['name', ]

    name = models.CharField(max_length=1024, unique=True, blank=False)

    def __str__(self):
        return f"({self.pk}) {self.name}"

class Product(models.Model):
    class Meta:
        verbose_name = "Товар"
        verbose_name_plural = "Товары"
        ordering = ['name', 'published', 'deleted']
    name = models.CharField(max_length=1024, unique=True, blank=False)
    description = models.CharField(max_length=4096, default="")
    categories = models.ManyToManyField(Category)
    price = models.IntegerField(default=0)
    deleted = models.BooleanField(default=False)
    published = models.BooleanField(default=False)

    @property
    def category_names(self):
        return (cat.name for cat in self.categories.all())


    def __str__(self):
        return self.name



