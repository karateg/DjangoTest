from rest_framework import serializers
from .models import Product, Order
from django.contrib.auth.models import User


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'


class ProductSerializer(serializers.ModelSerializer):
    # author = serializers.SerializerMethodField()
    author = UserSerializer()
    class Meta:
        model = Product
        fields = ('pk', 'name', 'discount', 'discription', 'price', 'created_at', 'archived', 'author')


    # def get_author(self, obj):
    #     return obj.author.username

class OrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Order
        fields = ('adress', 'promo', 'user', 'products')