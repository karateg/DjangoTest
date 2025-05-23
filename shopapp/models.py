from django.db import models
from django.contrib.auth.models import User


# Create your models here.
class Product(models.Model):
    """
    Модель для представления товара
    Заказы: :model:`shopapp.Order` 
    """
    class Meta:
        ordering = ['name', 'price']
        verbose_name = 'Продукт'
        verbose_name_plural = 'Продукты'
    name = models.CharField(max_length=100)
    discription = models.TextField(null=False, blank= True)
    price = models.DecimalField(default=0, max_digits=8, decimal_places=2 )
    discount = models.PositiveSmallIntegerField(default=0)
    created_at = models.DateTimeField(auto_now_add=True)
    changed_at = models.DateTimeField(auto_now=True)
    archived = models.BooleanField(default=False)
    author = models.ForeignKey(User, on_delete=models.CASCADE, null=True, related_name='products', default=1)
    def __str__(self) -> str:
       return f'Товар {self.name}, pk={self.pk}'
    


class Order(models.Model):
    adress = models.TextField(null=True, blank=True)
    promo = models.CharField(max_length=20, null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(User, on_delete=models.PROTECT)
    products = models.ManyToManyField(Product, related_name='orders')


class Text(models.Model):
    sale = models.BooleanField(default=False)
    product = models.ForeignKey(Product, on_delete=models.DO_NOTHING)
    

    