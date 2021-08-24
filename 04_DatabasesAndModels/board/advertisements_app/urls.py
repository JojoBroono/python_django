from django.urls import path
from .views import AdvertisementList, AdvertisementDetailView

urlpatterns = [
    path('advertisements', AdvertisementList.as_view()),
    path('advertisements/<int:pk>', AdvertisementDetailView.as_view())
]
