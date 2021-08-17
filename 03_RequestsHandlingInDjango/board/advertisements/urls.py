from django.urls import path
from . import views

urlpatterns = [
    path('', views.MainView.as_view(), name='MainView'),
    path('advertisements', views.AdvertisementList.as_view(), name='AdvertisementList'),
    path('contacts', views.ContactsView.as_view(), name='contacts'),
    path('about', views.AboutView.as_view(), name='about'),
]
