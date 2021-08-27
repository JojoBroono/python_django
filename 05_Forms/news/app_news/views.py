from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.views import View
from django.views.generic import ListView
from .forms import NewsItemForm, NewCommentForm
from .models import NewsItem, Comment


class NewItemCreateView(View):
    def get(self, request):
        news_item_form = NewsItemForm()
        return render(request, 'app_news/create.html', context={'news_item_form': news_item_form})

    def post(self, request):
        news_item_form = NewsItemForm(request.POST)

        if news_item_form.is_valid():
            NewsItem.objects.create(**news_item_form.cleaned_data)
            return HttpResponseRedirect('/news')

        return render(request, 'app_news/create.html', context={'news_item_form': news_item_form})


class NewsItemEditFormView(View):
    def get(self, request, news_item_id):
        news_item = NewsItem.objects.get(id=news_item_id)
        news_item_form = NewsItemForm(instance=news_item)
        return render(request, 'app_news/edit.html', context={
            'news_item_form': news_item_form,
            'news_item_id': news_item_id
        })

    def post(self, request, news_item_id):
        news_item = NewsItem.objects.get(id=news_item_id)
        news_item_form = NewsItemForm(request.POST, instance=news_item)

        if news_item_form.is_valid():
            news_item.save()
            return HttpResponseRedirect('/news')

        return render(request, 'app_news/edit.html', context={
            'news_item_form': news_item_form,
            'news_item_id': news_item_id
        })


class NewsItemsListView(View):
    def get(self, request):
        news_items = NewsItem.objects.order_by('created_at')
        return render(request, 'app_news/news_items_list.html', context={
            'news_items': news_items
        })


class NewsItemDetailView(View):
    def get(self, request, news_item_id):
        news_item = NewsItem.objects.get(id=news_item_id)
        comments = news_item.comment_set.all()
        comment_form = NewCommentForm()
        return render(request, 'app_news/news_item_detail.html', context={
            'news_item': news_item,
            'comments': comments,
            'comment_form': comment_form
        })

    def post(self, request, news_item_id):
        news_item = NewsItem.objects.get(id=news_item_id)
        comment_form = NewCommentForm(request.POST)

        if comment_form.is_valid():
            comment_data = comment_form.cleaned_data
            comment_data['news_item'] = news_item
            Comment.objects.create(**comment_data)

        comments = news_item.comment_set.all()
        return render(request, 'app_news/news_item_detail.html', context={
            'news_item': news_item,
            'comments': comments,
            'comment_form': comment_form
        })