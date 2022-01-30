
from django.contrib import admin
from django.urls import path
from product.views import ProductAPIView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/v1/productlist', ProductAPIView.as_view()),
]
