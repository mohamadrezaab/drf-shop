import factory
from core.product.models import Category, Brand, Product, ProductLine, ProductImage



class CategoryFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Category
        
    name = factory.sequence(lambda n:"Category_%d" %n)


class BrandFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Brand
        
    name = factory.sequence(lambda n:"Category_%d" %n)

    
class ProductFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Product
        
    name = "test_product" 
    description = 'test_descripstion'
    is_digital = True
    category = factory.SubFactory(CategoryFactory)
    brand = factory.SubFactory(BrandFactory)
    
   
class ProductLineFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = ProductLine
        
    price = '10.00'
    sku = '12345'
    stock_qty  = 1
    product = factory.SubFactory(ProductFactory)
    is_active  = True
    
    
class ProductImageFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = ProductImage
        
    alternative_text = 'test altrnative text'
    url = 'test.jpg'
    prodcutline = factory.SubFactory(ProductLineFactory)
        
    
    