from django.shortcuts import render
from django.http import HttpResponse


def advertisements_list(request):
    return HttpResponse(
        '<ul>'
        '<li>Мастер на час</li>'
        '<li>Выведение из запоя</li>'
        '<li>Услуги экскаватора-погрузчика, гидромолота, ямобура</li>'
        '</ul>'
    )
