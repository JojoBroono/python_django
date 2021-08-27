from django import forms
from .models import NewsItem, Comment


class NewsItemForm(forms.ModelForm):
    class Meta:
        model = NewsItem
        fields = '__all__'


class NewCommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['user_name', 'content']
