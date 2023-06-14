from django.shortcuts import render

def newsPage(request):
    return render(request , 'news.html')