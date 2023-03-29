import factory
from core.product.models import Category, Brand, Product



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