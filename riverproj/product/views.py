from rest_framework.viewsets import ModelViewSet

from .models import Category, Product
from .serializers import CategorySerializer, ProductSerializer

class CategoryViewSet(ModelViewSet):
    serializer_class = CategorySerializer
    queryset = Category.objects.all()

class ProductViewSet(ModelViewSet):
    serializer_class = ProductSerializer
    queryset = Product.objects.all()

