"""
URL configuration for storefront project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
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
from .settings import DEBUG, argv, environ

admin.site.site_header = "Storefront Admin"
admin.site.site_title = "Storefront Admin Portal"
admin.site.index_title = "Welcome to Storefront Admin Portal"

urlpatterns = [
    path('admin/', admin.site.urls),
    path('playground/', include('apps.playground.urls')),
    path('store/', include('apps.store.urls')),
    path('auth/', include('djoser.urls')),
    path('auth/', include('djoser.urls.jwt')),
]

# add debug toolbar
TESTING = "test" in argv or "PYTEST_VERSION" in environ

if not TESTING and DEBUG: 
    urlpatterns.append(path('__debug__/', include('debug_toolbar.urls')))