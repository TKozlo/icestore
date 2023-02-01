"""store URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
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
from django.conf.urls.static import static
from django.conf import settings
from rest_framework.authtoken.views import obtain_auth_token

from orders.views import stripe_webhook_view
from products.views import *
 

urlpatterns = [
    path('admin/', admin.site.urls),

    path('', IndexView.as_view(), name='index'),
    path('products/', include('products.urls')),
    path('users/', include(('users.urls', 'users'), namespace='users')),
    path('accounts/', include('allauth.urls')),
    path('dop/', include('dop.urls')),
    path('blog/', include('blog.urls')), 
    path('orders/', include('orders.urls')),
    path('webhook/stripe/', stripe_webhook_view, name='stripe_webhook'),

    path('api/', include('api.urls')),
    path('api-token-auth/', obtain_auth_token),

    path('ckeditor/', include('ckeditor_uploader.urls')),
    ]


if settings.DEBUG:
    urlpatterns.append(path('__debug__/', include('debug_toolbar.urls')))
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)