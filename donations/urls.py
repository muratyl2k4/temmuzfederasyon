from django.urls import path

from .views import donationsPage , donationPage
urlpatterns = [ 
    path('bagislar' , donationsPage) , 
    path('bagislar/<int:pk>' , donationPage)
] 