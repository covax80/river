
from django.contrib import admin
from django.urls import path
from product.views import ProductListAPIView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/v1/productlist', ProductListAPIView.as_view()),
    path('api/v1/product/<int:pk>', ProductDetailAPIView.as_view()),
]
