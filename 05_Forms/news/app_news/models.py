from django.db import models
from django.contrib.auth.models import User, AnonymousUser


class NewsItem(models.Model):
    title = models.CharField(max_length=1000)
    content = models.TextField()
    created_at = models.DateField(auto_now_add=True)
    updated_at = models.DateField(auto_now=True)

    is_active = models.BooleanField(default=True)

    def __str__(self):
        if self.is_active:
            active_status = "active"
        else:
            active_status = "not active"
        return f"{self.title}, {self.created_at}, {active_status}"


class Comment(models.Model):
    user = models.ForeignKey(User, null=True, on_delete=models.CASCADE)
    user_name = models.CharField(max_length=100)
    content = models.TextField()
    news_item = models.ForeignKey('NewsItem', null=False, on_delete=models.CASCADE)

    def display_content(self):
        if len(self.content) <= 15:
            return self.content[:15]
        else:
            return self.content[:15] + '...'

    def __str__(self):
        if self.user is not None:

            return f"{self.user.username}: {self.content[:15]}..."
        else:
            return f"{self.user_name} (Anonymous): {self.content[:15]}..."
