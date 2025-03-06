from django.db import models
from django.contrib.auth.models import User


# Create your models here.
class Product(models.Model):
    """
    Модель для представления товара
    """
    class Meta:
        # ordering = ['name', 'price']
        verbose_name = 'Продукт'
        verbose_name_plural = 'Продукты'
    name = models.CharField(max_length=100)
    discription = models.TextField(null=False, blank= True)
    # price = models.DecimalField(default=0, max_digits=8, decimal_places=2 )
    discount = models.PositiveSmallIntegerField(default=0)
    created_at = models.DateTimeField(auto_now_add=True)
    changed_at = models.DateTimeField(auto_now=True)
    archived = models.BooleanField(default=False)
    # author = models.ForeignKey(User, on_delete=models.CASCADE, null=True, related_name='products', default=1)
    def __str__(self) -> str:
       return self.name
    
    
class Shop(models.Model):
    name = models.CharField(max_length=50)
    
    class Meta:
        verbose_name = 'Магазин'
        verbose_name_plural = 'Магазины'

    def __str__(self):
        return self.name
    
class ShopItem(models.Model):

    shop = models.ForeignKey(Shop, on_delete=models.PROTECT, related_name='shops')
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='products')
    price = models.DecimalField(default=0, max_digits=8, decimal_places=2, verbose_name='Цена' )
    quantity = models.PositiveIntegerField(default=0)

    class Meta:
        verbose_name = 'Товар'
        verbose_name_plural = 'Товары'


class Client(models.Model):
    user = models.OneToOneField(User, on_delete= models.CASCADE)
    name = models.CharField(max_length=100, verbose_name='Имя клиента')
    balance = models.PositiveIntegerField(default=0, verbose_name='Баланс')
    status = models.PositiveIntegerField(default=0, verbose_name='Статус')

    class Meta:
        verbose_name = 'Клиент'
        verbose_name_plural = 'Клиенты'

    def __str__(self):
        return self.name

