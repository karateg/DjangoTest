from django.shortcuts import render,redirect, reverse
from django.http import HttpResponse, HttpRequest
from timeit import default_timer

from django.contrib.auth.models import Group
from shopapp.forms import OrderForm, ProductForm
from shopapp.models import Product, Order

def shop_index(request: HttpRequest):

    products = [('apple','1000'), ('orange', '500'), ('juice', '500')]

    dict1 = {
        'time_runing': default_timer(),
        'products': products,
    }

    return render(request, 'shopapp/index.html', context = dict1)

def group_list(request: HttpRequest):
    context = {
        'groups': Group.objects.prefetch_related('permissions').all()
    }
    return render( request ,'shopapp/group-list.html', context= context)

def products_list(requst: HttpRequest):
    context = {
        'products': Product.objects.all()
    }
    return render(requst,'shopapp/products-list.html', context= context)

def create_product(request: HttpRequest) -> HttpResponse:
    if request.method == "POST":
        form = ProductForm(request.POST)
        if form.is_valid():
            # name = form.cleaned_data['name']
            # price = form.cleaned_data['price']
            # Product.objects.create(name=name, price=price)

            # Product.objects.create(**form.cleaned_data)
            form.save()
            url = reverse('shopapp:products_list')
            return redirect(url)
    else:
        form = ProductForm()
    context = {
        'form': form
    }
    return render(request, 'shopapp/create_product.html', context= context )


def orders_list(requst: HttpRequest):
    context = {
        'orders': Order.objects.select_related('user').prefetch_related('products').all()
    }
    return render(requst,'shopapp/orders-list.html', context= context)

def create_list(request: HttpRequest):
    if request.method == "POST":
        form = OrderForm(request.POST)
        if form.is_valid():
            form.save()
            url = reverse('shopapp:orders_list')
            return redirect(url)
    else:
        form = OrderForm()
    context = {
        'form': form
    }
    return render(request, 'shopapp/order-create.html', context= context)