from rest_framework import serializers

from .models import Category, Product


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        # fields = ('name', 'description', 'categories', 'price', 'deleted', 'published')
        fields = ('name', 'description', 'category_names', 'price', 'deleted', 'published')
