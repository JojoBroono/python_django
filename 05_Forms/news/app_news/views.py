from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponseRedirect, HttpResponse
from django.shortcuts import render
from django.views import View
from django.views.generic import ListView, DetailView
from .forms import NewsItemForm, NewCommentForm, AuthForm, NewCommentFormAnon
from .models import NewsItem, Comment
from django.views.generic.edit import CreateView, UpdateView
from django.contrib.auth.views import LoginView, LogoutView
from django.contrib.auth.models import User, AnonymousUser


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
        if request.user.is_authenticated:
            comment_form = NewCommentForm()
        else:
            comment_form = NewCommentFormAnon()
        return render(request, 'app_news/news_item_detail.html', context={
            'news_item': news_item,
            'comments': comments,
            'comment_form': comment_form
        })

    def post(self, request, news_item_id):
        news_item = NewsItem.objects.get(id=news_item_id)
        if request.user.is_authenticated:
            comment_form = NewCommentForm(request.POST)
            user = request.user
        else:
            comment_form = NewCommentFormAnon(request.POST)
            user = None

        if comment_form.is_valid():
            comment_data = comment_form.cleaned_data
            comment_data['news_item'] = news_item
            comment_data['user'] = user
            Comment.objects.create(**comment_data)

        comments = news_item.comment_set.all()

        return render(request, 'app_news/news_item_detail.html', context={
            'news_item': news_item,
            'comments': comments,
            'comment_form': comment_form
        })


class LogInView(LoginView):
    template_name = 'app_news/login.html'


class LogOutView(LogoutView):
    template_name = 'app_news/logout.html'
    next_page = '/news/'