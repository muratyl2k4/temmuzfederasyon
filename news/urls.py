from django.urls import path 
from .views import newsPage
urlpatterns = [
    path('haberler' , newsPage) , 

    #path('haberler/<int:id>' , newPage)
]
