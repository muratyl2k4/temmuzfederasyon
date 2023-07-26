from django import template
from genel_baskanlik.models import Yonetim_Kurulu

from django.utils.html import format_html

register = template.Library()

turkiye_illeri = [
        ["01", "Adana"],
        ["02", "Adıyaman"],
        ["03", "Afyon"],
        ["04", "Ağrı"],
        ["05", "Amasya"],
        ["06", "Ankara"],
        ["07", "Antalya"],
        ["08", "Artvin"],
        ["09", "Aydın"],
        ["10", "Balıkesir"],
        ["11", "Bilecik"],
        ["12", "Bingöl"],
        ["13", "Bitlis"],
        ["14", "Bolu"],
        ["15", "Burdur"],
        ["16", "Bursa"],
        ["17", "Çanakkale"],
        ["18", "Çankırı"],
        ["19", "Çorum"],
        ["20", "Denizli"],
        ["21", "Diyarbakır"],
        ["22", "Edirne"],
        ["23", "Elazığ"],
        ["24", "Erzincan"],
        ["25", "Erzurum"],
        ["26", "Eskişehir"],
        ["27", "Gaziantep"],
        ["28", "Giresun"],
        ["29", "Gümüşhane"],
        ["30", "Hakkari"],
        ["31", "Hatay"],
        ["32", "Isparta"],
        ["33", "Mersin"],
        ["34", "İstanbul"],
        ["35", "İzmir"],
        ["36", "Kars"],
        ["37", "Kastamonu"],
        ["38", "Kayseri"],
        ["39", "Kırklareli"],
        ["40", "Kırşehir"],
        ["41", "Kocaeli"],
        ["42", "Konya"],
        ["43", "Kütahya"],
        ["44", "Malatya"],
        ["45", "Manisa"],
        ["46", "Kahramanmaraş"],
        ["47", "Mardin"],
        ["48", "Muğla"],
        ["49", "Muş"],
        ["50", "Nevşehir"],
        ["51", "Niğde"],
        ["52", "Ordu"],
        ["53", "Rize"],
        ["54", "Sakarya"],
        ["55", "Samsun"],
        ["56", "Siirt"],
        ["57", "Sinop"],
        ["58", "Sivas"],
        ["59", "Tekirdağ"],
        ["60", "Tokat"],
        ["61", "Trabzon"],
        ["62", "Tunceli"],
        ["63", "Şanlıurfa"],
        ["64", "Uşak"],
        ["65", "Van"],
        ["66", "Yozgat"],
        ["67", "Zonguldak"],
        ["68", "Aksaray"],
        ["69", "Bayburt"],
        ["70", "Karaman"],
        ["71", "Kırıkkale"],
        ["72", "Batman"],
        ["73", "Şırnak"],
        ["74", "Bartın"],
        ["75", "Ardahan"],
        ["76", "Iğdır"],
        ["77", "Yalova"],
        ["78","Karabük"],
        ["79", "Kilis"],
        ["80", "Osmaniye"],
        ["81", "Düzce"]
    ]
@register.simple_tag
def x():
    text = ''
    for a in turkiye_illeri:
        text+= '<li><a class="dropdown-item col-3" href="../iller/{}">{} - {}</a></li>'.format(a[1]  ,a[0] , a[1])
    
    
    return format_html(text)
gb = Yonetim_Kurulu.objects.get(id=5)
@register.simple_tag
def y():
    text = f'<li style="margin-left:10%; width: 30%;"><a href="../genelbaskanlik" class="dropdown-item"><p class="" style="font-size:24px; font-family:"Montserrat" ,sans-serif;">Emre ŞAHİN</p><hr class="w-50 mx-auto"> <img style="width:40%;" src="../{gb.Yonetici_Resmi}" > <p class="mt-2" style="font-size:20px;">Genel Başkan</p></a></li>'
    return format_html(text)
