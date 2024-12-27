from django.core.management import BaseCommand
from django.contrib.auth.models import User
from shopapp.models import Order, Product



class Command(BaseCommand):
    def handle(self, *args, **options):
        self.stdout.write("Создание заказа")
        agent = User.objects.get(username='admin')
        order = Order.objects.get_or_create(
            adress='Горького 1',
            promo='sale',
            user=agent,
        )
        self.stdout.write(f"Заказ {order} создан")
