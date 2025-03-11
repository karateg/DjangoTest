from django.test import TestCase
from django.urls import reverse
import json
# Create your tests here.
class GetCookieViewTestCase(TestCase):
    
    def test_get_cookie(self):
        response = self.client.get(reverse('test_auth:cookie-get'))
        self.assertContains(response, 'Cookie value')
    
class FooBarViewTestCase(TestCase):

    def test_foo_bar(self):
        response = self.client.get((reverse('test_auth:foo-bar')))
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.headers['content-type'], 'application/json')

        content_data = {'foo': 'bar', 'number': '123'}
        received_data = json.loads(response.content)
        self.assertEqual(received_data, content_data)
