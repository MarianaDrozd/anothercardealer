"""django_views_practice URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
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
from src.django_cardealer.views import MainPageTemplateView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', MainPageTemplateView.as_view(),),
    path('cars/', include('src.apps.cars.urls', namespace='cars')),
    path('dealers/', include('src.apps.dealers.urls', namespace='dealers')),
    path('orders/', include('src.apps.orders.urls', namespace='orders')),
    path('newsletters/', include('src.apps.newsletters.urls', namespace='newsletters')),
    path('', include("src.apps.users.urls")),
    path('users/', include('django.contrib.auth.urls'))
]
