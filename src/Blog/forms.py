from django import forms
from django.forms.forms import Form

from .models import Article

class ArticleForm(forms.ModelForm):

    title   = forms.CharField(label='Article Title', widget = forms.TextInput(attrs={'placeholder' : 'Your Article'}))
    content = forms.CharField(
        widget = forms.Textarea(attrs={
            'placeholder' : 'Article Text',
            'class'       : 'new-article-class',
            'id'          : 'id_for_textarea',
            'rows'        : 40,
            'cols'        : 60
        }))

    active = forms.BooleanField()

    class Meta:
        model = Article
        fields = [
            'title',
            'content',
            'active'
        ]