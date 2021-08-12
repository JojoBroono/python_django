from django.urls import path
from . import views

urlpatterns = [
    path("", views.advertisements_list, name='advertisements'),
    path("advertisement", views.advertisement, name='advertisement_detailed')
]
