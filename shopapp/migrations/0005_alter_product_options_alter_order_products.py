# Generated by Django 5.1.4 on 2024-12-28 08:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shopapp', '0004_order_products'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='product',
            options={'ordering': ['name', 'price'], 'verbose_name': 'Продукт', 'verbose_name_plural': 'Продукты'},
        ),
        migrations.AlterField(
            model_name='order',
            name='products',
            field=models.ManyToManyField(related_name='orders', to='shopapp.product'),
        ),
    ]
