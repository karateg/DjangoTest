from django.shortcuts import get_object_or_404, render,redirect, reverse
from django.http import HttpResponse, HttpRequest, HttpResponseRedirect
from timeit import default_timer
from django.urls import reverse_lazy
from django.views import View
from django.contrib.auth.models import Group
from shopapp.forms import GroupForm, OrderForm, ProductForm
from shopapp.models import Product, Order
from django.views.generic import TemplateView, ListView, DetailView, CreateView, UpdateView, DeleteView

class ShopIndexView(View):

    def get(self, request: HttpRequest) -> HttpResponse:
        products = [('apple','1000'), ('orange', '500'), ('juice', '500')]

        dict1 = {
            'time_runing': default_timer(),
            'products': products,
        }
        return render(request, 'shopapp/index.html', context = dict1)


# def shop_index(request: HttpRequest):

#     products = [('apple','1000'), ('orange', '500'), ('juice', '500')]

#     dict1 = {
#         'time_runing': default_timer(),
#         'products': products,
#     }

#     return render(request, 'shopapp/index.html', context = dict1)

# def group_list(request: HttpRequest):
#     context = {
#         'groups': Group.objects.prefetch_related('permissions').all()
#     }
#     return render( request ,'shopapp/group-list.html', context= context)


class GroupsListView(View):

    def get(self, request: HttpRequest) -> HttpResponse:
        context = {
            'form': GroupForm,
            'groups': Group.objects.prefetch_related('permissions').all(),
        }
        return render( request ,'shopapp/group-list.html', context= context)
    
    def post(self, request: HttpRequest) -> HttpResponse:
        form = GroupForm(request.POST)
        if form.is_valid():
            form.save()
        return redirect(request.path)
        


def products_list(requst: HttpRequest):
    context = {
        'products': Product.objects.all()
    }
    return render(requst,'shopapp/products-list.html', context= context)


class ProductListView(ListView):
    template_name = 'shopapp/products-list.html'
    # model = Product
    queryset = Product.objects.filter(archived=False)
    context_object_name = 'products'
    # def get_context_data(self, **kwargs):
    #     context = super().get_context_data(**kwargs)
    #     context['products'] = Product.objects.all()
    #     return context


# class ProductDetailView(View):

#     def get(self, requst: HttpRequest, pk: int) -> HttpResponse:
#         product = get_object_or_404(Product, pk=pk)
#         context = {
#             'product': product,
#         }
#         return render(requst, "shopapp/prooducts-details.html", context= context)

class ProductDetailView(DetailView):
    template_name = 'shopapp/prooducts-details.html'
    model = Product
    context_object_name = 'product'
    



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


class ProductCreateView(CreateView):
    model = Product
    fields = 'name', 'price', 'discription', 'discount'
    # form_class = ProductForm
    success_url = reverse_lazy('shopapp:products_list')


class ProductUpdateView(UpdateView):
    model = Product
    fields = 'name', 'price', 'discription', 'discount'
    template_name_suffix = '_update'
    def get_success_url(self):
        return reverse('shopapp:products_ditails', kwargs={'pk': self.object.pk})


class ProductDeleteView(DeleteView):
    model = Product
    success_url = reverse_lazy('shopapp:products_list')

    def form_valid(self, form):
        success_url = self.get_success_url()
        self.object.archived = True
        self.object.save()
        return HttpResponseRedirect(success_url)    
    


def orders_list(requst: HttpRequest):
    context = {
        'orders': Order.objects.select_related('user').prefetch_related('products').all()
    }
    return render(requst,'shopapp/orders-list.html', context= context)


class OrderListView(ListView):
    # model = Order
    queryset = (
        Order.objects.select_related('user').prefetch_related('products')
        )
    

class OrderDetailView(DetailView):
    # model = Order
    queryset = (
        Order.objects.select_related('user').prefetch_related('products')
        )

# def create_list(request: HttpRequest):
#     if request.method == "POST":
#         form = OrderForm(request.POST)
#         if form.is_valid():
#             form.save()
#             url = reverse('shopapp:order_list')
#             return redirect(url)
#     else:
#         form = OrderForm()
#     context = {
#         'form': form
#     }
#     return render(request, 'shopapp/order-create.html', context= context)

class OrderCreateView(CreateView):
    model = Order
    form_class = OrderForm
    success_url = reverse_lazy('shopapp:orders_list')
    

class OrderUpdateView(UpdateView):
    model = Order
    form_class = OrderForm
    template_name = 'shopapp/order_update.html'
    def get_success_url(self):
        return reverse('shopapp:orders_ditails', kwargs={'pk': self.object.pk})
    
class OrderDeleteView(DeleteView):
    model = Order
    success_url = reverse_lazy('shopapp:orders_list')
