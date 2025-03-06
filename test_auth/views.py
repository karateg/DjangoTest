from django.shortcuts import render, redirect, reverse
from django.contrib.auth.decorators import login_required, permission_required
from django.contrib.auth import authenticate, login, logout
from django.http import HttpRequest, HttpResponse
from django.contrib.auth.views import LogoutView
from django.urls import reverse_lazy
from django.views import View
from django.views.generic import TemplateView, CreateView
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.decorators.cache import cache_page
from django.utils.translation import gettext_lazy as _, ngettext
from .models import Profile
from random import random


# Create your views here.


class HelloView(View):
    message = _('Hello world!')
    def get(self,request):

        items = request.GET.get('items') or 0
        items = int(items)
        products = ngettext(
            'one product',
            "{count} products",
            items
        )

        products = products.format(count=items)


        return HttpResponse(
            f'<h1> {self.message} </h1>'
            f'\n<h2> {products} </h2>'
        )


class ProfileView(TemplateView):
    template_name = 'test_auth/profile.html'


class RegisterView(CreateView):
    form_class = UserCreationForm
    template_name = 'test_auth/register.html'
    success_url = reverse_lazy('test_auth:profile')

    def form_valid(self, form):
        response = super().form_valid(form)

        Profile.objects.create(user=self.object)

        username = form.cleaned_data.get('username')
        password = form.cleaned_data.get('password2')
        user = authenticate(self.request, username=username, password=password)
        login(request=self.request, user=user)

        return response
    


def login_view(request: HttpRequest):
    if request.method == "GET":
        if request.user.is_authenticated:
            return redirect('/admin/')
        return render(request, 'test_auth/login.html')
    username = request.POST['username']
    password = request.POST['password']

    user = authenticate(request, username=username, password=password)

    if user is not None:
        login(request, user)
        redirect('/admin/')
        
    return render(request, 'test_auth/login.html', {'error': 'Invalid login credentials'})

def logout_view(request: HttpRequest):
    logout(request)
    return redirect(reverse('test_auth:login'))

class TestLogoutView(LogoutView):
    next_page = reverse_lazy('test_auth:login')


def set_cookie_view(request: HttpRequest) -> HttpResponse:
    responce = HttpResponse('Cookie_set')
    responce.set_cookie('new', 'info', max_age=3600)
    return responce

@cache_page(30)
def get_cookie_view(request: HttpRequest) -> HttpResponse:
    value = request.COOKIES.get('new', 'default info')
    return HttpResponse(f'Cookie value: {value} + {random()}')

@permission_required('test_auth.view_profile', raise_exception=True)
def set_session_view(request: HttpRequest) -> HttpResponse:
    request.session['new'] = 'new_info'
    return HttpResponse('Session set')

@login_required
def get_session_view(request: HttpRequest) -> HttpResponse:
    value = request.session.get('new', 'default info')
    return HttpResponse(f'Session value: {value}')
