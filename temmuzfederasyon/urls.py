
from django.contrib import admin
from django.urls import path , include

urlpatterns = [
    path('' , include('main.urls')),
    path('' , include('accounts.urls')),
    path('' , include('donations.urls')),
    path('admin/', admin.site.urls),
    ]
'''
path('' , include('news.urls')),
path('' , include('genel_baskanlik.urls')),
path('' , include('teskilat.urls')),
path('' , include('sehitler.urls')),
path('' , include('kurumsal.urls')),
'''
