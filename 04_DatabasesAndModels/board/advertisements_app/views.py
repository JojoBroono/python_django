from django.shortcuts import render
from django.views.generic import ListView, DetailView
from .models import Advertisement


class AdvertisementList(ListView):
    model = Advertisement


class AdvertisementDetailView(DetailView):
    model = Advertisement

    def get_object(self, queryset=None):
        obj = super().get_object(queryset=None)
        obj.views_count += 1
        obj.save()
        return obj
