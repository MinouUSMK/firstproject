from django import forms
from .models import Article


class ArticleForm(forms.ModelForm):
    class Meta:
        model = Article
        fields = ['title','content']

#class ArticleForm(forms.Form):
 #   title=forms.CharField()
  #  content=forms.TimeField()

