from django.shortcuts import render
from sehitler.models import Sehit
# Create your views here.

def homePage(request):
    

    sehit_objects = Sehit.objects.all()

    data = {'sehitler' : sehit_objects}


    return render(request , 'home.html',data)
