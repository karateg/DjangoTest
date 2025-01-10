from django.urls import path
from request_app.views import porcess_get,user_form, upload_file

app_name = "request_app"

urlpatterns = [
    path('get/', porcess_get, name= "get-view"),
    path('info/', user_form, name= "user-info"),
    path('file-upload/', upload_file, name= "file-upload"),
]