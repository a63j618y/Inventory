from django.shortcuts import render
from django.http import HttpResponse


# def index(request, id, nickname):
def index(request):
    # if 'id' in request.GET:
    #     id = request.GET['id']
    #     result = 'you typed : "' + id + '".'
    # else:
    #     result = 'please send msg parameter'
    # result = 'your id: ' + str(id) + ', name: "' + nickname + '".'
    params = {
        'title': 'Hello/Index',
        'msg': 'これはサンプル',
        'goto': 'next',
    }
    # return HttpResponse(request, 'hello/index.html')
    return render(request, 'inventory/index.html', params)


def next(request):
    params = {
        'title': 'hello/Next',
        'msg': 'これは、次のページ',
        'goto': 'index',
    }
    return render(request, 'inventory/index.html', params)
