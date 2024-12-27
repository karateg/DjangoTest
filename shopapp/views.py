from django.shortcuts import render
from django.http import HttpResponse, HttpRequest
from timeit import default_timer
from django.contrib.auth.models import Group
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


def orders_list(requst: HttpRequest):
    context = {
        'orders': Order.objects.all()
    }
    return render(requst,'shopapp/orders-list.html', context= context)