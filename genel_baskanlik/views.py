from django.shortcuts import render
from .models import Yonetim_Kurulu , Denetim_Kurulu , Disiplin_Kurulu , Yurutme_Kurulu
def generalPresidencyPage(request):
    return render(request , 'general_presidency.html')

boardCase = {
    'yonetim-kurulu' : Yonetim_Kurulu , 
    'yurutme-kurulu' : Yurutme_Kurulu , 
    'denetim-kurulu' : Denetim_Kurulu , 
    'disiplin-kurulu' : Disiplin_Kurulu , 
}
def boardPage(request , kurul):
    board_object = boardCase[kurul].objects.all()
    data = {
        'kurul' : board_object , 
        'link_kurul' : kurul
    }
    return render(request , 'board.html' , data)

def managerPage(request ,kurul ,  id ):
    manager_object = boardCase[kurul].objects.get(id=id)
    data = {
        'manager' : manager_object
    }
    return render(request , 'manager.html' , data)