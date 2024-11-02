import datetime
import os

from django.shortcuts import render

from django.http import HttpResponse
from django.shortcuts import render, reverse
#
#
def home_view(request):
    template_name = 'app/home.html'
#     # впишите правильные адреса страниц, используя
#     # функцию `reverse`
    pages = {
        'Главная страница': reverse('home'),
        'Показать текущее время': datetime.datetime.now(),
        'Показать содержимое рабочей директории': os.listdir()
    }
#
    # context и параметры render менять не нужно
    # подбробнее о них мы поговорим на следующих лекциях
    context = {
        'pages': pages
    }
    return render(request, template_name, context)

#



def time_view(request):
    # обратите внимание – здесь HTML шаблона нет,
    # возвращается просто текст
    current_time = datetime.datetime.now()
    msg = f'Текущее время:{current_time}'
    return HttpResponse(msg)
#
#
def workdir_view(request):
    # по аналогии с `time_view`, напишите код,
    # который возвращает список файлов в рабочей
    # директории
    list = os.listdir()
    List_1 = f'Список файлов:{list}'
    return HttpResponse(List_1)
    raise NotImplemented