from django.urls import path 
from .views import sehit_page, sehitler_page


urlpatterns = [
    path('sehitler',sehitler_page),
    path('sehitler/<int:id>',sehit_page)
]