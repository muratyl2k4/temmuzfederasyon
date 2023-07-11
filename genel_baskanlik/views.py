from django.shortcuts import render , redirect , HttpResponseRedirect
from django.urls import reverse
from teskilat.views import managerPage as teskilat_mp
from .models import Yonetim_Kurulu , Denetim_Kurulu , Disiplin_Kurulu , Yurutme_Kurulu

def generalPresidencyPage(request):
    return render(request , 'general_presidency.html')

boardCase = {
    'yonetim-kurulu' : [Yonetim_Kurulu , 'YÖNETİM KURULU'] , 
    'yurutme-kurulu' : [Yurutme_Kurulu , 'YÜRÜTME KURULU'] ,
    'denetim-kurulu' : [Denetim_Kurulu , 'DENETİM KURULU' ] , 
    'disiplin-kurulu' : [Disiplin_Kurulu  , 'DİSİPLİN KURULU' ], 
}
def boardPage(request , kurul):
    
    board_object = boardCase[kurul][0].objects.all()
   
    data = {
        'kurul' : board_object , 
        'link_kurul' : kurul , 
        'kurul_isim' : boardCase[kurul][1]
    }
    return render(request , 'board.html' , data)

def managerPage(request, kurul, id):
    try:
        manager_object = boardCase[kurul][0].objects.get(id=id)
    except KeyError:
        return teskilat_mp(request ,kurul , id)

    data = {
        'manager': manager_object
    }
    return render(request, 'manager.html', data)