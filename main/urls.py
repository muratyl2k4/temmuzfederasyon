from django.urls import path 
from .views import homePage , contactPage
urlpatterns = [
    path('' , homePage , name='home'),
    path('home' , homePage , name='home'),
    path('iletisim' , contactPage , name='contact')
]