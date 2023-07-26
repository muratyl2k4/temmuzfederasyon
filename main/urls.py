from django.urls import path 
from .views import homePage , contactPage , pols
urlpatterns = [
    path('' , homePage , name='home'),
    path('home' , homePage , name='home'),
    path('iletisim' , contactPage , name='contact'),
    path('policy' , pols)
]

