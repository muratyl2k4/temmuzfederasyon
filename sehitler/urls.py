from django.urls import path 
from .views import sehitler_page


urlpatterns = [
    path('sehitler',sehitler_page)
]