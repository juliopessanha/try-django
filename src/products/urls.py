from django.urls import path

#from pages.views import home_view, contact_view, about_view
from products.views import (
    product_detail_view, 
    product_create_view, 
    product_google_search_view, 
    dynamic_lookup_view, 
    product_delete_view, 
    product_list_view,
    )

appname = 'products' #namespaces

urlpatterns = [
    path('', product_detail_view),
    path('<int:my_id>/', dynamic_lookup_view, name = 'product-detail'),
    path('<int:my_id>/delete/', product_delete_view, name = 'product-delete'),
    path('create/', product_create_view),
    path('list/', product_list_view, name = 'product-list'),
    path('search/', product_google_search_view),
]
