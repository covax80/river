from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet
from rest_framework import exceptions as api_exceptions, status

from .models import Category, Product
from .serializers import CategorySerializer, ProductSerializer

class CategoryViewSet(ModelViewSet):
    serializer_class = CategorySerializer
    queryset = Category.objects.all()

    def perform_destroy(self, instance):
        occupied_categories = []
        for prod in Product.objects.all():
            for cat in prod.categories.all():
                if cat.id not in occupied_categories:
                    occupied_categories.append(cat.id)
        if instance.id in occupied_categories:
            raise api_exceptions.NotAcceptable("Not allow to remove the category with Product link")
            # return Response(status=status.HTTP_424_FAILED_DEPENDENCY)
        else:
            super().perform_destroy(instance)
            return Response(status=status.HTTP_204_NO_CONTENT)



class ProductViewSet(ModelViewSet):
    serializer_class = ProductSerializer
    queryset = Product.objects.all()




