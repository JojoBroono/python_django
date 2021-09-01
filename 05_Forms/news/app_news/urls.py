from django.urls import path, include
from django.contrib import admin
from .views import NewItemCreateView, NewsItemEditFormView, NewsItemsListView, NewsItemDetailView

urlpatterns = [
    path('create/', NewItemCreateView.as_view()),
    path('<int:pk>/edit/', NewsItemEditFormView.as_view(), name="news_item_edit"),
    path('', NewsItemsListView.as_view()),
    path('<int:news_item_id>/', NewsItemDetailView.as_view()),
]
