from django.contrib import admin
from django.urls import path
from shop import views
# from shop.views import Products_page


urlpatterns = [
    path('tracker', views.tracker, name='tracker'),
    path('search', views.search, name='search'),
    path('productadd', views.productadd, name='productadd'),
    path('checkout', views.checkout, name='checkout'),
    path('products', views.products_page, name='products'),
    path('accessories', views.accessories_page, name='accessories'),
    # path('products', Products_page.as_view(), name='products'),

]
