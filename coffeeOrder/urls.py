"""coffeeOrder URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include, re_path
from products import views as products_views
from carts import views as carts_views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    re_path(r'^$', products_views.product, name='home'),
    re_path(r'^s/$', products_views.search, name='search'),
    re_path(r'^products/$', products_views.all, name='products'),
    re_path(r'^products/(?P<slug>[\w-]+)/$', products_views.single, name='single_product'),
    re_path(r'^cart/(?P<slug>[\w-]+)/$', carts_views.add_to_cart, name='add_to_cart'),
    re_path(r'^cart/(?P<id>\d+)/$', carts_views.remove_from_cart, name='remove_from_cart'),
    re_path(r'^cart/', carts_views.view, name='cart'),
    re_path(r'^admin/', admin.site.urls),
    re_path(r'^accounts/', include('django.contrib.auth.urls')),
    #path('', include('orders.urls')),
]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)