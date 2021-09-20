from django import forms
from .models import NewsItem, Comment


class NewsItemForm(forms.ModelForm):
    class Meta:
        model = NewsItem
        fields = '__all__'


class NewCommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['content']


class NewCommentFormAnon(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['user_name', 'content']

class AuthForm(forms.Form):
    username = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput)
