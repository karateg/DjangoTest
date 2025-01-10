from django.shortcuts import render
from django.http import HttpResponse, HttpRequest
from django.core.files.storage import FileSystemStorage
# Create your views here.

def porcess_get(requst: HttpRequest) -> HttpResponse:
    a = requst.GET.get('a', '')
    b = requst.GET.get('b', '')
    result = a + b
    context = {
        'a': a,
        'b': b,
        'result': result,
    }
    return render(requst, 'request_app/request_query_params.html', context= context)


def user_form(requst: HttpRequest) -> HttpResponse:
    return render(requst, 'request_app/user-form.html')


def upload_file(requst: HttpRequest) -> HttpResponse:
    if requst.method == 'POST' and requst.FILES.get('myfile'):
        myfile = requst.FILES['myfile']
        fs = FileSystemStorage()
        if myfile.size > 1 * pow(1024,2):
            return render(requst, 'request_app/file-upload.html', {'error': 'Размер файла превышает 1 MB.'})
        filename = fs.save(myfile.name, myfile)
        print("Файл сохранен", filename)
        return render(requst,  'request_app/file-upload.html', {'success': 'Файл успешно загружен.'})
    return render(requst,  'request_app/file-upload.html')
