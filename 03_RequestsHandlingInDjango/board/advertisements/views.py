from django.shortcuts import render
from django.views import View
from django.views.generic import TemplateView
from django.http import HttpResponse


class MainView(View):
    regions = ['Moscow', 'Tanzania', 'Jamaica']
    categories = ['Computers', 'Auto', 'Music']

    def get(self, request):
        return render(request, 'advertisements/main_form.html', {
            'regions': MainView.regions,
            'categories': MainView.categories
        })


class AdvertisementList(View):
    post_counter = 0
    advertisements = [
        'Мастер на час',
        'Выведение из запоя',
        'Услуги экскаватора-погрузчика, гидромолота, ямобура'
    ]

    def get(self, request):
        return render(request, 'advertisements/advertisement_list.html', {'adv': AdvertisementList.advertisements})

    def post(self, request):
        AdvertisementList.post_counter += 1
        return HttpResponse(f"Success! POST requests done: {AdvertisementList.post_counter}")


class AboutView(TemplateView):
    template_name = "advertisements/about.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['name'] = 'ООО Яндекс'
        context['description'] = 'Яндекс — поисковая система и интернет-портал.'
        return context


class ContactsView(TemplateView):
    template_name = "advertisements/contacts.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['address'] = 'Москва, ул. Льва Толстого, 16'
        context['phone_number'] = '+7 495 739-37-77'
        context['email'] = 'pr@yandex-team.ru'
        return context
