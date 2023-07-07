from django.urls import path
from .views import citiesPage , cityPage
urlpatterns = [
    path('iller' , citiesPage , name='iller'),
    
    path('iller/<str:city>' , cityPage , name='il') , 
]