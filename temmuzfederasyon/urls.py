
from django.contrib import admin
from django.urls import path , include , re_path 
from django.conf.urls.static import static
from django.conf import settings
admin.autodiscover()
urlpatterns = [
    path('' , include('main.urls')),
    path('' , include('accounts.urls')),
    path('' , include('donations.urls')),
    path('' , include('sehitler.urls')),
    path('' , include('news.urls')),
    path('' , include('kurumsal.urls')),
    path('' , include('genel_baskanlik.urls')),
    path('' , include('teskilat.urls')),
    path('' , include('temmuz15gecesi.urls')),
    

    path('admin/', admin.site.urls),
    ]
urlpatterns += static(settings.MEDIA_URL , document_root = settings.MEDIA_ROOT)
'''
path('' , include('genel_baskanlik.urls')),
'''
