from django.test import TestCase
from django.urls import reverse

from mysite import settings
from shopapp.models import Product, Order
from .utils import add_two_numbers
from django.contrib.auth.models import User
from string import ascii_letters
from random import choices
# Create your tests here.
class AddTwoNumbersTestCase(TestCase):
    
    def test_add_two_numbers(self):
        result = add_two_numbers(2, 3)
        self.assertEqual(result, 5)

class ProductCreateViewTestCase(TestCase):
    
    def setUp(self):
        self.user = User.objects.create(username='Jgon')
        self.product_name = ''.join(choices(ascii_letters, k=10))
        Product.objects.filter(name=self.product_name).delete()

    def tearDown(self):
        self.user.delete()

    def test_create_porduct(self):
        responce = self.client.post(
            reverse('shopapp:products_create'),
            {
                'name': self.product_name,
                'price':"10000",
                'discription': "a new phone",
                'discount': '10',
                'author': self.user,
            }
        )

        self.assertRedirects(responce, reverse('shopapp:products_list'))

        self.assertTrue(Product.objects.filter(name=self.product_name).exists())


class OrderCreateViewTestCase(TestCase):

    def setUp(self):
        self.user = User.objects.create(username='Anton')

    def tearDown(self):
        self.user.delete()

    def test_create_order(self):
        responce = self.client.post(
             reverse('shopapp:orders_create'),
             {
                 "user": "user", 
                 "adress": 'Minina 5', 
                 "products": ["apple","orange"], 
                 'promo': 'sale',
             }
        )

        self.assertRedirects(responce, reverse('shopapp:orders_list'))
        # self.assertEqual(responce.status_code, 200)


class OrderDeleteViewTestCase(TestCase):

    def setUp(self):
        
        self.user = User.objects.create(username='User')
        self.order = Order.objects.create(
            user=self.user,
            adress='Antonovka',
            promo='Promo'
        )
        

    def tearDown(self):
        Order.objects.filter(user=self.user).delete()
        self.user.delete()
        self.order.delete()


    def test_order_delete(self):
        self.assertTrue(Order.objects.filter(pk=self.order.pk).exists())

        response = self.client.post(
            reverse('shopapp:orders_delete', kwargs={'pk': self.order.pk})
        )

        self.assertEqual(response.status_code, 302)

        self.assertIn(str(reverse('shopapp:orders_list')), response.url)

        self.assertFalse(Order.objects.filter(pk=self.order.pk).exists())


class ProductDetailViewTestCase(TestCase):

    @classmethod
    def setUpClass(cls):
        cls.user = User.objects.create(username='Jgon')
        cls.product = Product.objects.create(
            name="Phone",
            author=cls.user,
            )
        print('Юзер создан')

    # def setUp(self):
    #     self.user = User.objects.create(username='Jgon')
    #     self.product = Product.objects.create(
    #         name="Phone",
    #         author=self.user,
    #         )

    @classmethod
    def tearDownClass(cls):
        cls.product.delete()
        cls.user.delete()

    # def tearDown(self):
    #     self.product.delete()
    #     self.user.delete()

    def test_get_product(self):
        response = self.client.get(
            reverse('shopapp:products_ditails', kwargs={'pk':self.product.pk})
        )
        self.assertEqual(response.status_code, 200)
        

    def test_get_product_2(self):
        response = self.client.get(
            reverse('shopapp:products_ditails', kwargs={'pk':self.product.pk})
        )
        self.assertContains(response, self.product.name)


class OrdersListViewTestCase(TestCase):

    @classmethod
    def setUpClass(cls):
        cls.data = dict(
            username='Jhon',
            password='Qwerty',
        )
        cls.user = User.objects.create_user(**cls.data)

    @classmethod
    def tearDownClass(cls):
        cls.user.delete()

    def setUp(self):
        # self.client.login(**self.data)
        self.client.force_login(self.user)

    def test_orders_list(self):
        responce = self.client.get(reverse('shopapp:orders_list'))
        self.assertContains(responce,"Заказы")

    def test_view_not_authenticated(self):
        self.client.logout()
        responce = self.client.get(reverse('shopapp:orders_list'))
        # self.assertRedirects(responce, str(settings.LOGIN_URL))
        self.assertEqual(responce.status_code, 302)
        self.assertIn(str(settings.LOGIN_URL), responce.url)

