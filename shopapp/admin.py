from django.contrib import admin

from shopapp.admin_mixins import Export_goods_mixin
from .models import Order, Product
from django.http import HttpRequest
from django.db.models import QuerySet
# Register your models here.

class OrderInline(admin.TabularInline):
    model = Product.orders.through

@admin.action(description='Безопасное удаление')
def mark_archived(modeladmin: admin.ModelAdmin, requst: HttpRequest, qveryset: QuerySet):
    qveryset.update(archived=True)


@admin.action(description='Востоновление')
def unmark_archived(modeladmin: admin.ModelAdmin, requst: HttpRequest, qveryset: QuerySet):
    qveryset.update(archived=False)


@admin.action(description='Установка скидки 5%%')
def set_discount(modeladmin: admin.ModelAdmin, requst: HttpRequest, qveryset: QuerySet):
    qveryset.filter(discount=0).update(discount=5)


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin, Export_goods_mixin):

    actions = [
        mark_archived,
        unmark_archived,
        'export_csv',
        set_discount,
    ]

    inlines = [
        OrderInline,
    ]
    list_display = 'pk', 'name', 'discription_short', 'price', 'discount'
    list_display_links =  'pk', 'name'
    ordering = ['-pk']
    search_fields = 'name', 'discription'

    fieldsets = [
        (None, {
            'fields': ('name', 'discription')
        }),
        ('Настройка цены',{
            'fields': ('price', 'discount'),
            'classes': ('collapse',)
        }),
        ('Дополнительные опции',{
            'fields': ('archived',),
            'classes': ('collapse',),
            'description':'Безопасное удаление'
        }),
    ]

    def discription_short(self, obj: Product) -> str:
        if len(obj.discription) < 50:
            return obj.discription
        return obj.discription[:50] + "..."


class PrdouctInline(admin.TabularInline):
    model = Order.products.through
    

@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):

    inlines = [
        PrdouctInline,
    ]

    list_display = 'pk', 'adress', 'promo', 'created_at', 'user_name'
    list_display_links = 'pk', 'adress'

    def get_queryset(self, request):
        return Order.objects.select_related('user')
    

    def user_name(self,obj: Order) -> str:
        return obj.user.first_name or obj.user.username
    
