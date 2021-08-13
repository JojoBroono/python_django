from django.shortcuts import render
from django.http import HttpResponse


def home(request):
    return render(request, 'advertisements/i_sell_homework.html')


def advertisements_list(request):
    return render(request, 'advertisements/advertisements_list.html')


def advertisement(request):
    return render(request, 'advertisements/advertisement.html')


def python_basic(request):
    return render(request, 'advertisements/python-basic.html')


def django_framework(request):
    return render(request, 'advertisements/django.html')


def os_linux(request):
    return render(request, 'advertisements/os-linux.html')


def sql(request):
    return render(request, 'advertisements/sql.html')


def web_layout(request):
    return render(request, 'advertisements/web-layout.html')

