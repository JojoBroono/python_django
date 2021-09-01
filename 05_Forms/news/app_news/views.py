from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.views import View
from django.views.generic import ListView, DetailView
from .forms import NewsItemForm, NewCommentForm
from .models import NewsItem, Comment
from django.views.generic.edit import CreateView, UpdateView


class NewItemCreateView(CreateView):
    model = NewsItem
    template_name = 'app_news/create.html'
    form_class = NewsItemForm

    def get_success_url(self):
        return f'/news/{self.object.id}/'


class NewsItemEditFormView(UpdateView):
    model = NewsItem
    template_name = 'app_news/edit.html'
    form_class = NewsItemForm

    def get_success_url(self):
        return f'/news/{self.object.id}/'


class NewsItemsListView(ListView):
    template_name = 'app_news/news_items_list.html'
    model = NewsItem

    def get_context_data(self, *, object_list=None, **kwargs):
        context = {
            'object_list': self.object_list.order_by('created_at')
        }
        return context


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

