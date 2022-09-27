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
    name = models.CharField(max_length=1024, unique=True, blank=False, verbose_name="Товар")
    description = models.CharField(max_length=4096, default="", verbose_name="Описание", blank=True)
    categories = models.ManyToManyField(Category, verbose_name="Категории")
    price = models.IntegerField(default=0, verbose_name="Цена")
    deleted = models.BooleanField(default=False, verbose_name="Удалён")
    published = models.BooleanField(default=False, verbose_name="Опубликован")

    @property
    def category_names(self):
        return (cat.name for cat in self.categories.all())

    def show_categories_admin(self):
        result = sorted(list(self.category_names))
        return "; ".join(result)
    show_categories_admin.short_description = "В категориях"

    def __str__(self):
        return self.name



