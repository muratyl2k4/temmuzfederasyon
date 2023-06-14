from django.urls import path
from .views import donationPage
urlpatterns = [ 
    path('bagislar' , donationPage)
]