from django.shortcuts import render
from django.views.generic import ListView, DetailView
from .models import Advertisement


class AdvertisementList(ListView):
    model = Advertisement


class AdvertisementDetailView(DetailView):
    model = Advertisement
