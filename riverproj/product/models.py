from django.db import models

# Create your models here.

class Category(models.Model):
    class Meta:
        verbose_name = "Категория товара"
        verbose_name_plural = "Категории товаров"
        ordering = ['name', ]

    name = models.CharField(max_length=1024, unique=True, blank=False)
    def __str__(self):
        return f"({self.pk}) {name}"

class Product(models.Model):
    class Meta:
        verbose_name = "Товар"
        verbose_name_plural = "Товары"
        ordering = ['name', 'published', 'deleted']
    name = models.CharField(max_length=1024, unique=True, blank=False)
    description = models.TextField(default="")
    price = models.IntegerField(default=0)
    deleted = models.BooleanField(default=False)
    published = models.BooleanField(default=False)

    def __str__(self):
        return self.name
    """
    def categories(self):
        return (cat.name for cat in Category.objects.filter( \
                product = self.pk))
    """



class CategoryLink(models.Model):
    class Meta:
        verbose_name = "Связь Товар-Категория"
        verbose_name_plural = "Связи Товар-Категория"
        ordering = ['category', 'product']
    product = models.ForeignKey("Product", on_delete=models.DO_NOTHING)
    category = models.ForeignKey("Category", on_delete=models.DO_NOTHING)



