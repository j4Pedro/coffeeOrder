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
from django.urls import path, include
from products import views as products_views
from carts import views as carts_views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', products_views.product, name='home'),
    path('search/', products_views.search, name='search'),
    path('products/', products_views.all, name='products'),
    path('products/<slug>/', products_views.single, name='single_product'),
    path('cart/<slug>/', carts_views.update_cart, name='update_cart'),
    path('cart/', carts_views.view, name='cart'),
    path('admin/', admin.site.urls),
    path('accounts/', include('django.contrib.auth.urls')),
    #path('', include('orders.urls')),
]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)