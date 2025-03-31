from django.db.models.signals import post_save, post_delete
from django.dispatch import receiver

from .models import Text, Product

@receiver(post_save, sender=Product)
def create_product(sender, instance, created, **kwargs ):
    if created:
        Text.objects.get_or_create(
            sale = True,
            product= instance,
        )

@receiver(post_delete, sender=Product)
def delete_product(sender, instance, **kwargs ):
    Text.objects.filter(
        product=instance
    ).delete()