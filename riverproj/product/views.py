from rest_framework import generics
from riverproj.product.serializers import ProductSerializer
from .models import Product


class ProductAPIView(generics.ListAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer