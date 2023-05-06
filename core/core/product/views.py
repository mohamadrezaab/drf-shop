from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.response import Response
from .models import Category, Brand, Product
from .serializers import CategorySerializers, BrandSerializers, ProductSerializers
from drf_spectacular.utils import extend_schema
from rest_framework.decorators import action
from django.db import connection
from pygments import highlight
from pygments.formatters import TerminalFormatter
from pygments.lexers import SqlLexer
from sqlparse import format



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
    #queryset = Product.isactive.all()
    queryset = Product.objects.all().isactive()
    lookup_field = 'slug'
    
    
    def retrieve(self, request, slug=None):
        serializer = ProductSerializers(self.queryset.filter(slug=slug).select_related('category'), many=True)
        data =  Response(serializer.data) 
        q = list(connection.queries)
        print(len(q))
        for qs in q:
            sqlformatted = format(str(qs['sql']), reindent=True)
            print(highlight(sqlformatted, SqlLexer(), TerminalFormatter()))
            
        return data
    
    
    @extend_schema(responses=ProductSerializers)
    def list(self, request):
        serializer = ProductSerializers(self.queryset, many=True)
        return Response(serializer.data)

    @action(
        methods=['get'],
        detail=False,
        url_path=r"category/(?P<slug>[\w-]+)/all",
        url_name="all",
    )
    def list_product_by_category_slug(self, request, slug=None): 
        """
            An endpoint to return products by category
        """
        
        serializer = ProductSerializers(
            self.queryset.filter(category__slug=slug), many=True
        )
        return Response(serializer.data)
