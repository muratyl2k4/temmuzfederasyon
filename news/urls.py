from django.urls import path 
from .views import newsPage , newPage
urlpatterns = [
    path('haberler' , newsPage) , 
    path('haberler/<int:id>' , newPage)
]
