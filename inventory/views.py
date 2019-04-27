from django.shortcuts import render
from django.http import HttpResponse
from .form import HelloForm


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
        # 'goto': 'next',
        'form': HelloForm()
    }
    if(request.method == 'POST'):
        params['message'] = '名前：' + request.POST['name'] + \
            '<br>メール：' + request.POST['mail'] + \
            '<br>年齢：' + request.POST['age']
        params['form'] = HelloForm(request.POST)

    # return HttpResponse(request, 'hello/index.html')
    return render(request, 'inventory/index.html', params)


# def next(request):
#     params = {
#         'title': 'hello/Next',
#         'msg': 'これは、次のページ',
#         'goto': 'index',
#     }
#     return render(request, 'inventory/index.html', params)


def form(request):
    msg = request.POST['msg']
    params = {
        'title': 'hello/Next',
        'msg': 'こんにちは、' + msg + 'さん。',
    }
    return render(request, 'inventory/index.html', params)
