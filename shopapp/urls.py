from django.urls import path
from .views import ShopIndexView, GroupsListView, ProductDetailView, ProductListView, OrderListView, OrderDetailView, ProductCreateView, ProductUpdateView, ProductDeleteView,OrderCreateView, OrderDeleteView ,OrderUpdateView

app_name = "shopapp"

urlpatterns = [
    path('', ShopIndexView.as_view(), name= "index"),
    path('groups/', GroupsListView.as_view() ,name= "groups_list"),
    path('products/', ProductListView.as_view() ,name= "products_list"),
    path('products/<int:pk>/',ProductDetailView.as_view(),name= "products_ditails"),
    path('products/<int:pk>/update/',ProductUpdateView.as_view(),name= "products_update"),
    path('products/<int:pk>/confirm-delete/',ProductDeleteView.as_view(),name= "products_delete"),
    path('products/create/', ProductCreateView.as_view() ,name= "products_create"),
    path('orders/', OrderListView.as_view() ,name= "orders_list"),
    path('orders/<int:pk>/', OrderDetailView.as_view() ,name= "orders_ditails"),
    path('orders/<int:pk>/update/', OrderUpdateView.as_view(), name='orders_update'),
    path('orders/<int:pk>/delete/',OrderDeleteView.as_view(),name= "orders_delete"),
    path('orders/create/', OrderCreateView.as_view() ,name= "orders_create"),
    
]