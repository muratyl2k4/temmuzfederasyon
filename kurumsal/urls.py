from django.urls import path 
from .views import institutionalPage
urlpatterns = [
    path('kurumsal' , institutionalPage )
]