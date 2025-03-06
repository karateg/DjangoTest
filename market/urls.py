from django.urls import path
from rest_framework.routers import DefaultRouter
from .views import AboutMeView,ClientUpdateView, wallet_up, ProductListView,ProductDetailView

app_name = "market"


urlpatterns = [
    path('client/<int:pk>/', AboutMeView.as_view(), name='client_info'),
    path('client/<int:pk>/update/', ClientUpdateView.as_view(), name='client_update'),
    path('client/<int:pk>/wallet_up/', wallet_up, name='wallet_up'),
    path('products/', ProductListView.as_view(), name='products'),
    path('products/<int:pk>/', ProductDetailView.as_view(), name='product_ditails'),
]