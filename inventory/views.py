from django.shortcuts import render
from django.http import HttpResponse


def index(request, id, nickname):
    # if 'id' in request.GET:
    #     id = request.GET['id']
    #     result = 'you typed : "' + id + '".'
    # else:
    #     result = 'please send msg parameter'
    result = 'your id: ' + str(id) + ', name: "' + nickname + '".'
    return HttpResponse(result)

