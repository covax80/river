from rest_framework.routers import DefaultRouter
from django.urls import path

from .views import CategoryViewSet, ProductViewSet


app_name = 'product'

router = DefaultRouter()

router.register(r'product', ProductViewSet, basename='product')
router.register(r'category', CategoryViewSet, basename='category')

urlpatterns = router.urls





