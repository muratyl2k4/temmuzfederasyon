from django.db import models

class Kurumsal(models.Model):
    Federasyon_Aciklama_Title = models.CharField(max_length=200)
    Federasyon_Aciklama_Text = models.TextField()

    Federasyon_Misyon_Title = models.CharField(max_length=200)
    Federasyon_Misyon_Text = models.TextField()
    
    Federasyon_Vizyon_Title = models.CharField(max_length=200)
    Federasyon_Vizyon_Text = models.TextField()


