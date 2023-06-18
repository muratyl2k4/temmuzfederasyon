from django.shortcuts import render
from .models import Bagis
# Create your views here.

def donationsPage(request):
    donations = Bagis.objects.all()

    data = { 
        'donation' : donations
    }
    return render(request , 'donations.html' , data)

def donationPage(request , pk):
    donation = Bagis.objects.get(pk=pk)
    data = {
        'donation' : donation
     }
    return render(request , 'donation.html' , data)