from django.shortcuts import render
from sehitler.models import Sehit



def sehitler_page(request):

    sehit_objects = Sehit.objects.all()

    data = {'sehitler' : sehit_objects}


    return render(request,'sehitler.html',data)
# Create your views here.
