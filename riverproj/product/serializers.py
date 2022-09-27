from rest_framework import serializers

from .models import Category, Product


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ('name', 'description', 'categories', 'price', 'deleted', 'published')
        # fields = ('name', 'description', 'category_names', 'price', 'deleted', 'published')

    def validate_categories(self, value):
        if not (2 <= len(value) <= 10):
            raise serializers.ValidationError(f"Count of categories = {len(value)}. It's not in from 2 to 10 range")
        return value

    def validate_price(self, value):
        if not (-1 < value < 1000000):
            raise serializers.ValidationError(f"Price {value} not correct (0<=price<=1000000)")
        return value

