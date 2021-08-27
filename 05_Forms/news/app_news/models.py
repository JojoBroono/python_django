from django.db import models


class NewsItem(models.Model):
    title = models.CharField(max_length=1000)
    content = models.TextField()
    created_at = models.DateField(auto_now_add=True)
    updated_at = models.DateField(auto_now=True)

    is_active = models.BooleanField(default=True)

    def __str__(self):
        return self.title


class Comment(models.Model):
    user_name = models.CharField(max_length=100)
    content = models.TextField()
    news_item = models.ForeignKey('NewsItem', null=False, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.user_name}: {self.content[:30]}..."

