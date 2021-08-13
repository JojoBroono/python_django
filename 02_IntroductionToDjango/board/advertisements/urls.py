from django.urls import path
from . import views

urlpatterns = [
    path("", views.home, name='i_sell_homework'),
    path("python-basic", views.python_basic, name='python-basic'),
    path("django", views.django_framework, name='django-framework'),
    path("os-linux", views.os_linux, name='os-linux'),
    path("sql", views.sql, name='sql'),
    path("web-layout", views.web_layout, name='web-layout')

]
