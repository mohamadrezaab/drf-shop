from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.response import Response
from .models import Category, Brand, Product
from .serializers import CategorySerializers, BrandSerializers, ProductSerializers
from drf_spectacular.utils import extend_schema


class CategoryViewSet(viewsets.ViewSet):
    """
        A Viewset for viwing all categories
    """
    queryset = Category.objects.all()

    
    @extend_schema(responses=CategorySerializers)
    def list(self, request):
        serializer = CategorySerializers(self.queryset, many=True)
        return Response(serializer.data)
    

class BrandViewSet(viewsets.ViewSet):
    """
        A Viewset for viwing all brands
    """
    queryset = Brand.objects.all()
    
    @extend_schema(responses=BrandSerializers)
    def list(self, request):
        serializer = BrandSerializers(self.queryset, many=True)
        return Response(serializer.data)
    



class ProductViewSet(viewsets.ViewSet):
    """
        A Viewset for viwing all products
    """
    queryset = Product.objects.all()
    
    @extend_schema(responses=ProductSerializers)
    def list(self, request):
        serializer = ProductSerializers(self.queryset, many=True)
        return Response(serializer.data)
    
