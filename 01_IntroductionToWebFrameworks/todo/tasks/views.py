from django.http import HttpResponse

from django.views import View
import random


class ToDoView(View):

    def get(self, request, *args, **kwargs):
        todo_list = [
            '<li>Установить python</li>',
            '<li>Установить django</li>',
            '<li>Запустить сервер</li>',
            '<li>Порадоваться результату</li>',
            '<li>Зайти во views.py и добавить один элемент li</li>',
            '<li>Встать в 6 утра</li>',
            '<li>Выйти на пробежку</li>',
            '<li>Плотно позавтракать</li>',
            '<li>Улыбнуться солнышку</li>',
            '<li>Выпить чаю</li>',
        ]
        amount_of_tasks = 8
        total_amount_of_tasks = min(amount_of_tasks, len(todo_list))
        unique_tasks_indexes = random.sample(range(len(todo_list)), total_amount_of_tasks)

        response_html = "<ul>" + "".join(todo_list[i] for i in unique_tasks_indexes) + "</ul>"
        return HttpResponse(response_html)
