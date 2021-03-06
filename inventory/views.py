from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import TemplateView
from .forms import InventoryForm


class InventoryView(TemplateView):
    def __init__(self):
        self.params = {
            'title': 'Hello',
            'message': 'your date',
            'form': InventoryForm()
        }

    def get(self, request):
        return render(request, 'inventory/index.html', self.params)

    def post(self, request):
        msg = 'あなたは<b>' + request.POST['name'] + \
            '(' + request.POST['age'] + \
            'メールアドレス：' + request.POST['mail'] + \
            'です。' + request.POST['nullCheck'] + request.POST['choice'] + \
            'ラジオは' + request.POST['radio'] + \
            '複数選択は' + str(request.POST.getlist('multi'))

        if('check' in request.POST):
            msg += 'Checked!!'
        else:
            msg += 'not Checked!!'
        self.params['message'] = msg
        self.params['form'] = InventoryForm(request.POST)
        return render(request, 'inventory/index.html', self.params)


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
        'form': InventoryForm()
    }
    if(request.method == 'POST'):
        params['message'] = '名前：' + request.POST['name'] + \
            '<br>メール：' + request.POST['mail'] + \
            '<br>年齢：' + request.POST['age']
        params['form'] = InventoryForm(request.POST)

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
