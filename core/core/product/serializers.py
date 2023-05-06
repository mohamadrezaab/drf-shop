from rest_framework import serializers
from .models import Brand, Category, Product, ProductLine



class CategorySerializers(serializers.ModelSerializer):
    category_name = serializers.CharField(source='name')
    
    class Meta:
        model = Category
        fields = ("category_name",)
                
class BrandSerializers(serializers.ModelSerializer):
    class Meta:
        model = Brand
        exclude = ("id",)
        

class ProductLineSerializers(serializers.ModelSerializer):
    class Meta:
        model = ProductLine
        exclude = ('id', 'product', 'is_active')

                
        
class ProductSerializers(serializers.ModelSerializer):
    brand_name = serializers.CharField(source='brand.name')
    category_name = serializers.CharField(source='category.name')
    product_line = ProductLineSerializers(many=True)
    
    class Meta:
        model = Product
        fields = ( 
            "name",
            "slug",
            "description",
            "brand_name",
            "category_name",
            "product_line",
        )
        
