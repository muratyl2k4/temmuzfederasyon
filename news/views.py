from django.shortcuts import render
from .models import New
def newsPage(request):
    news = New.objects.all()
    data = { 
        'news' : news
    }    
    return render(request , 'news.html' ,data)

def newPage(request , id):
    new = New.objects.get(id=id)
    data = {
        'new' : new
    }
    return render(request , 'new.html' , data)