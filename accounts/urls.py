from django.urls import path
from .views import loginPage
urlpatterns = [
    path('giris' , loginPage)
]