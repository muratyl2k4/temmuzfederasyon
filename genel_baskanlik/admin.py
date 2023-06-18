from django.contrib import admin
from .models import Yonetim_Kurulu , Denetim_Kurulu , Disiplin_Kurulu , Yurutme_Kurulu

admin.site.register(Yonetim_Kurulu)
admin.site.register(Disiplin_Kurulu)
admin.site.register(Yurutme_Kurulu)
admin.site.register(Denetim_Kurulu)
# Register your models here.
