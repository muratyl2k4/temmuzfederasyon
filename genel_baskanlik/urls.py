from django.urls import path , include , re_path
from .views import generalPresidencyPage , boardPage , managerPage
urlpatterns = [
    path('genelbaskanlik' , generalPresidencyPage) , 
    path('genelbaskanlik/<str:kurul>' , boardPage) , 
    path('<str:kurul>/<int:id>' , managerPage) , 
    
]