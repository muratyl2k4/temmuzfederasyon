from django.urls import path
from .views import citiesPage , cityPage , managerPage , districtPage

app_name = 'teskilat'
urlpatterns = [
    path('iller' , citiesPage , name='iller'),
    
    path('iller/<str:city>' , cityPage , name='il') , 
    path('<str:city>/<int:id>' ,  managerPage) , 
    path('<str:city>/ilceler' ,  districtPage,) , 
    
]