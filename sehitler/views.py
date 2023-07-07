from django.shortcuts import render
from sehitler.models import Sehit



def sehitler_page(request):

    sehit_objects = Sehit.objects.all()

    data = {'sehitler' : sehit_objects}


    return render(request,'sehitler.html',data)
# Create your views here.

def sehit_page(request , id):
    sehit_object = Sehit.objects.get(id=id)
    data = {
        'sehit' : sehit_object
    }
    return render(request, 'sehit.html' , data)
