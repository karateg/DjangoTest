from rest_framework import serializers
from .models import Product, Order


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ('pk', 'name', 'discount', 'discription', 'price', 'created_at', 'archived')

class OrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Order
        fields = ('adress', 'promo', 'user', 'products')