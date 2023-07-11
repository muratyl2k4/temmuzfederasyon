from django.urls import path
from .views import temmuz15

urlpatterns = [ 
    path('15temmuzgecesi' , temmuz15 )
]