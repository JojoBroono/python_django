from django.shortcuts import render
from django.http import HttpResponse


def advertisements_list(request):
    return render(request, 'advertisements/advertisements_list.html')


def advertisement(request):
    return render(request, 'advertisements/advertisement.html')