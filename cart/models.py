from decimal import Decimal
from django.db import models

from market.models import ShopItem
from django.conf import settings
# Create your models here.


class Cart(object):

    def __init__(self, request):
        self.session = request.session
        cart = self.session.get(settings.CART_SESSION_ID)
        if not cart:
            cart = self.session[settings.CART_SESSION_ID] = {}
        self.cart = cart
    
    def add(self, product, shop, quantity=1, update_quantity=False):
        product_id = str(product.pk)

        if product_id not in self.cart:
            self.cart[product_id] = {
                'quantity': 0,
                'shop': str(shop),
                'price': str(product.price)
            }
        if update_quantity:
            self.cart[product_id]['quantity'] = quantity
        else:
            self.cart[product_id]['quantity'] += quantity

        self.save()

    def save(self):
        self.session[settings.CART_SESSION_ID] = self.cart
        self.session.modified = True

    def remove(self, product):
        product_id = product.pk

        if product_id in self.cart:
            del self.cart[product_id]
            self.save()

    def __iter__(self):
        product_ids = self.cart.keys()
        products = ShopItem.objects.filter(id__in=product_ids)

        for product in products:
            self.cart[str(product.id)]['product'] = product

        for item in self.cart.values():
            item['price'] = Decimal(item['price'])
            item['total_sum'] = item['price'] * item['quantity']
            yield item

    def __len__(self):
        return sum(item['quantity'] for item in self.cart.values())


    def get_total_sum(self):
        return sum(item['quantity'] * item['price'] for item in self.cart.values())
    
    def clear(self):
        del self.session[settings.CART_SESSION_ID]
        self.session.modified = True