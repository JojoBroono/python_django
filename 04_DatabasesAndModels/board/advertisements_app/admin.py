from django.contrib import admin

# Register your models here.
from .models import Advertisement, AdvertisementAuthor, AdvertisementCategory

admin.site.register(AdvertisementAuthor)
admin.site.register(AdvertisementCategory)
admin.site.register(Advertisement)