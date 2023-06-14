from django.shortcuts import render
from .models import Bagis
# Create your views here.

def donationPage(request):
    donations = Bagis.objects.all()

    data =  { 
        'donation' : donations
    }
    return render(request , 'donation.html' , data)