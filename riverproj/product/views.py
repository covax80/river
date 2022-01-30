from django.forms import model_to_dict
from rest_framework import generics
from rest_framework.views import APIView
from rest_framework.response import Response
from .serializers import ProductListSerializer
from .models import Product


class ProductListAPIView(generics.ListAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductListSerializer


class ProductAPIView(APIView):
    def get(self, request):
        product = Product.objects.get(pk=request.data['id'])
        return Response({'get': model_to_dict(product)})


    def post(self, request):
        new_product = Product.objects.create( \
            name = request.data['name'],
            description = request.data['description'],
        )
        return Response({'post': model_to_dict(new_product)})

    def delete(self, request):
        pass


"""
class ProductDetailAPIView(generics.GenericAPIView):
    pass

"""