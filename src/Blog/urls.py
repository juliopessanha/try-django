from django.urls import path

#from pages.views import home_view, contact_view, about_view
from Blog.views import create_article_view

appname = 'blog' #namespaces

urlpatterns = [
    path('create/', create_article_view),
]
