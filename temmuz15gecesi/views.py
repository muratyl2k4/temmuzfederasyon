from django.shortcuts import render
from .models import Temmuz15

def temmuz15(request):
    temmuz15_objs = Temmuz15.objects.all()
    data = {
        'temmuz15' : temmuz15_objs
    }
    return render(request , 'temm15.html' , data)