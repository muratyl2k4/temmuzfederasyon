from django.db import models

class Kurul(models.Model):
    Yonetici_Ismi = models.CharField(max_length=100 , null=True , blank=True)
    Yonetici_Sifati = models.CharField(max_length=100 , null=True , blank=True)
    Yonetici_Biyografi = models.TextField(null=True , blank=True)
    Yonetici_Resmi = models.ImageField(upload_to='djangouploads/genel_baskanlik/images/',null=True , blank=True)

    class Meta:
        abstract= True

    def __str__(self):
        return self.Yonetici_Ismi

class Yonetim_Kurulu(Kurul):
    def __init__(self, *args, **kwargs):
        for f in self._meta.fields:
            if f.attname == "parent_field":
                f.default = "child default"
        super(Yonetim_Kurulu, self).__init__(*args, **kwargs)

class Yurutme_Kurulu(Kurul):
    def __init__(self, *args, **kwargs):
        for f in self._meta.fields:
            if f.attname == "parent_field":
                f.default = "child default"
        super(Yurutme_Kurulu, self).__init__(*args, **kwargs)

class Denetim_Kurulu(Kurul):
    def __init__(self, *args, **kwargs):
        for f in self._meta.fields:
            if f.attname == "parent_field":
                f.default = "child default"
        super(Denetim_Kurulu, self).__init__(*args, **kwargs)

class Disiplin_Kurulu(Kurul):
    def __init__(self, *args, **kwargs):
        for f in self._meta.fields:
            if f.attname == "parent_field":
                f.default = "child default"
        super(Disiplin_Kurulu, self).__init__(*args, **kwargs)