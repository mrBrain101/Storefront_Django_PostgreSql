from decimal import Decimal
from rest_framework import serializers
from .models import Product, Collection


class CollectionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Collection
        fields = ['id', 'title', 'products_count']

    products_count = serializers.IntegerField(required=False)
    
    def create(self, validated_data):
        return Collection.objects.create(**validated_data)


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ['id', 'title', 'description', 'slug', 'inventory', 
                  'unit_price', 'price_with_tax', 'collection']
        
    price_with_tax = serializers.SerializerMethodField(method_name='calculate_tax')

    def calculate_tax(self, product : Product):
        return product.unit_price * Decimal(1.1)
    
    def create(self, validated_data):
        return Product.objects.create(**validated_data)