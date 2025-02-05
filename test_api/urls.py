from django.urls import path
from .views import hello_word, GroupListAPIView
app_name = 'test_api'

urlpatterns = [
    path('hello/', hello_word, name='hello'),
    path('groups/', GroupListAPIView.as_view(), name='groups')
]
