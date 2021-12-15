from django.http import Http404
from django.shortcuts import render, get_object_or_404, redirect

from .models import Product
from .forms import ProductForm, RawProductForm
# Create your views here.

#Get data using Django Form

# def product_create_view(request):
#     if request.method == 'POST':
#         form = RawProductForm(request.POST or None)
#         if form.is_valid(): #if the data is good
#             print(form.cleaned_data)
#             Product.objects.create(**form.cleaned_data) #saves on the database
#         else:
#             print(form.errors)
#     else:
#         form = RawProductForm()        

#     #if form.is_valid():
#     #    form.save()
#     #    form = ProductForm()

#     context = {
#         'form' : form
#     }
#     return( render(request, 'products/product_create.html', context))

def product_create_view(request):
    initial_data = {
        'description' : 'My Description is Incredible'
    }

    obj = Product.objects.get(id = 1)

    form = ProductForm(request.POST or None, initial = initial_data, instance = obj)
    if form.is_valid():
        form.save()
        form = ProductForm()

    context = {
        'form' : form
    }

    return( render(request, 'products/product_create.html', context) )

#Get data using pure HTML
def product_google_search_view(request):
    #print(request.POST)
    if request.method == 'POST':
        new_title = request.POST.get('title')
        print(new_title)
        #Product.objects.create(title = my_new_title)
    context = {}
    return( render(request, 'products/product_google_search.html', context))


def product_detail_view(request):
    obj = Product.objects.get(id = 1)
    context = {
        'object'         : obj
    }
    return( render(request, 'products/product_detail.html', context))

def dynamic_lookup_view(request, my_id):
    obj = get_object_or_404(Product, id = my_id)
    # try: #That's the same as above, but with more verbosity. Unecessary
    #     obj = Product.objects.get(id = my_id)
    # except Product.DoesNotExist:
    #     raise(Http404)
    context = {
        'object'         : obj
    }
    return( render(request, 'products/product_detail.html', context)) 

def product_delete_view(request, my_id):
    obj = get_object_or_404(Product, id = my_id)
    if request.method == 'POST':
        #Confirming delete
        obj.delete()
        return( redirect('../../') ) #Return to another page after deletion
    context = {
        'object' : obj
    }

    return( render(request, 'products/product_delete.html', context) )

def product_list_view(request):
    queryset = Product.objects.all()
    context = {
        'object_list' : queryset
    }

    return( render(request, 'products/product_list.html', context) )