from rest_framework import serializers
from .models import Brand, Category, Product, ProductLine, ProductImage



class CategorySerializers(serializers.ModelSerializer):
    category_name = serializers.CharField(source='name')
    
    class Meta:
        model = Category
        fields = ("category_name",)
                
class BrandSerializers(serializers.ModelSerializer):
    class Meta:
        model = Brand
        exclude = ("id",)
        

class ProductImageSerializers(serializers.ModelSerializer):
    class Meta:
        model = ProductImage
        exclude = ("id", "productline")

class ProductLineSerializers(serializers.ModelSerializer):
    product_image = ProductImageSerializers(many=True)
    
    class Meta:
        model = ProductLine
        fields = (
            "price",
            "sku",
            "stock_qty",
            "order",
            "product_image",
        )
                
        
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
        
