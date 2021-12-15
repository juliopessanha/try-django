from django.shortcuts import render, get_object_or_404, redirect

from .models import Article
from .forms import ArticleForm

# Create your views here.
def create_article_view(request):

    form = ArticleForm(request.POST or None)
    if form.is_valid():
        # process form data
        obj = Article() #gets new object
        obj.title = form.cleaned_data['title']
        obj.content = form.cleaned_data['content']
        obj.active = form.cleaned_data['active']
        #finally save the object in db
        obj.save()
        return( redirect('../../') )

    context = {
        'form' : form
    }
    return( render(request, 'articles/create_article.html', context) )