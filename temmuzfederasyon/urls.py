
from django.contrib import admin
from django.urls import path , include
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('' , include('main.urls')),
    path('' , include('accounts.urls')),
    path('' , include('donations.urls')),
    path('admin/', admin.site.urls),
    ]
urlpatterns += static(settings.MEDIA_URL , document_root = settings.MEDIA_ROOT)
'''
path('' , include('news.urls')),
path('' , include('genel_baskanlik.urls')),
path('' , include('teskilat.urls')),
path('' , include('sehitler.urls')),
path('' , include('kurumsal.urls')),
'''
