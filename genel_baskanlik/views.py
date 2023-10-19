from django.shortcuts import render 

from teskilat.views import managerPage as teskilat_mp
from .models import Yonetim_Kurulu , Denetim_Kurulu , Disiplin_Kurulu , Yurutme_Kurulu
from django.db.models import Q

def generalPresidencyPage(request):
    leader = Yonetim_Kurulu.objects.get(Yonetici_Ismi = "Emre ŞAHİN")
    data = { 
        'manager' : leader
    }
    return render(request , 'general_presidency.html' , data)

boardCase = {
    'yonetim-kurulu' : [Yonetim_Kurulu , 'YÖNETİM KURULU'] , 
    'yurutme-kurulu' : [Yurutme_Kurulu , 'YÜRÜTME KURULU'] ,
    'denetim-kurulu' : [Denetim_Kurulu , 'DENETİM KURULU' ] , 
    'disiplin-kurulu' : [Disiplin_Kurulu  , 'DİSİPLİN KURULU' ], 
}
def boardPage(request , kurul):
    
    board_object = boardCase[kurul][0].objects.all().order_by('id')
    baskan = None
    MF = None
    TE = None
    if boardCase[kurul][0] == Yonetim_Kurulu:
        baskan = board_object.get(Yonetici_Ismi = 'Emre ŞAHİN')
        MF = board_object[1:3]
        TE = board_object[3:5]
        
    data = {
        'kurul' : board_object , 
        'link_kurul' : kurul , 
        'kurul_isim' : boardCase[kurul][1] , 
        'baskan' : baskan , 
        'TE' : TE ,
        'MF' : MF
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