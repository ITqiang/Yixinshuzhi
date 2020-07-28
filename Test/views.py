# -*- coding: utf-8 -*-
from django.http import HttpResponse


def hello(request):
    print('hello')
    return HttpResponse("Hello world ! ")