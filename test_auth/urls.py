from django.contrib.auth.views import LoginView
from django.urls import path
from .views import (
    login_view, 
    logout_view, 
    TestLogoutView,
    set_cookie_view,
    get_cookie_view,
    set_session_view,
    get_session_view,
    ProfileView,
    RegisterView,
    HelloView,
    FooBarWiew,
)


app_name = 'test_auth'

urlpatterns = [
    # path('login/', login_view, name= "login"),
    path('login/', LoginView.as_view(
        template_name='test_auth/login.html',
        redirect_authenticated_user=True,                 
    ), name= "login"),
    path('logout/', logout_view, name= "logout"),
    # path('logout/', TestLogoutView.as_view(), name= "logout"),
    path('cookie/get/', get_cookie_view, name="cookie-get"),
    path('cookie/set/', set_cookie_view, name="cookie-set"),
    
    path('session/get/', get_session_view, name="session-get"),
    path('session/set/', set_session_view , name="session-set"),

    path('profile/', ProfileView.as_view(), name='profile'),
    path('register/', RegisterView.as_view(), name='register'),
    path('hello/', HelloView.as_view(), name='hello'),
    path('foo/', FooBarWiew.as_view(), name="foo-bar"),
    
]
