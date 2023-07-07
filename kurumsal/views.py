from django.shortcuts import render
from .models import Kurumsal
# Create your views here.
 
def institutionalPage(request):
    kurumsal = Kurumsal.objects.all().last()
    data = {
        'kurumsal' : kurumsal
    }
    return render(request ,'kurumsal.html' , data)