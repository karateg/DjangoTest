from django.core.management import BaseCommand
from shopapp.models import Product

class Command(BaseCommand):
    def handle(self, *args, **options):
        self.stdout.write("Создание продукта")
        products = ['apple', 'orange', 'juice']
        for product in products:
            new_product, created = Product.objects.get_or_create(name= product)
            if created:
                self.stdout.write(f'Продукт {new_product.name} создан')
        self.stdout.write(self.style.SUCCESS("Продукты созданы"))