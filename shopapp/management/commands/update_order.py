from django.core.management import BaseCommand
from shopapp.models import Order, Product



class Command(BaseCommand):
    def handle(self, *args, **options):
        order = Order.objects.first()
        products = Product.objects.all()
        for product in products:
            order.products.add(product)
        order.save()
        self.stdout.write(f"Добавленны товары {order.products.all()} в заказ {order}")