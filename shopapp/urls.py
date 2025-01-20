from django.urls import path
from .views import create_product, shop_index, group_list, products_list, orders_list, create_list

app_name = "shopapp"

urlpatterns = [
    path('', shop_index, name= "index"),
    path('groups/', group_list ,name= "groups_list"),
    path('products/', products_list ,name= "products_list"),
    path('products/create/', create_product ,name= "products_create"),
    path('orders/', orders_list ,name= "orders_list"),
    path('orders/create', create_list ,name= "orders_create"),
    
]