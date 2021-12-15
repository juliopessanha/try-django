from django.contrib import admin

from .models import Product
from Blog.models import Article
# Register your models here.

admin.site.register(Product)
admin.site.register(Article)