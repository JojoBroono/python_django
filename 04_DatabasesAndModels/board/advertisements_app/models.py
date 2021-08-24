from django.db import models
from django.utils.timezone import now


class AdvertisementAuthor(models.Model):
    name = models.CharField(max_length=1000)
    phone_number = models.CharField(max_length=12)
    email = models.EmailField()

    def __str__(self):
        return self.name


class AdvertisementCategory(models.Model):
    name = models.CharField(max_length=1000)

    def __str__(self):
        return self.name


class Advertisement(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField(default=None)
    publication_date = models.DateField(auto_now_add=True, null=True)
    end_date = models.DateField(default=now().date())
    price = models.IntegerField(default=0)
    views_count = models.IntegerField(default=0)

    author = models.ForeignKey('AdvertisementAuthor', on_delete=models.CASCADE, default=None, null=True)
    category = models.ForeignKey('AdvertisementCategory', on_delete=models.CASCADE, default=None, null=True)

    def __str__(self):
        return self.title
