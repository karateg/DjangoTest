from django.shortcuts import render
from django.http import HttpResponse, HttpRequest
import time


def set_useragent_middleware(get_responce):
    print('Запуск middleware')

    def middleware(request: HttpRequest):
        print('До запроса')
        request.user_agent = request.META['HTTP_USER_AGENT']
        responce = get_responce(request)
        print('После запроса')
        return responce
    
    return middleware

class CountRequestsMiddleware:


    def __init__(self, get_responce):
        self.get_responce = get_responce
        self.requst_count = 0
        self.responce_count = 0
        self.exception_count = 0
        
        self.last_request = {}
        self.time_limit = 1


    def __call__(self, requst: HttpRequest):
        # user_ip = requst.META['REMOTE_ADDR']
        # time_request = time.time()
        # if user_ip in self.last_request:
        #     time_between_requests = time_request - self.last_request[user_ip]
        #     if time_between_requests < self.time_limit:
        #         return render(requst, 'request_app/Error_429.html')
        # self.last_request[user_ip] = time_request
    
        self.requst_count += 1
        print('Количество запрсов = ', self.requst_count)
        responce = self.get_responce(requst)
        self.responce_count += 1
        print('Количество ответов = ', self.responce_count)
        return responce

    def process_exceptions(self, requst: HttpRequest, exeption: Exception):
        self.exception_count += 1
        print('Получили ошибку', self.exception_count)

