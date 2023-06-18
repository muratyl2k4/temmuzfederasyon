from django.db import models

class Sehit(models.Model):
    Sehit_Ismi = models.CharField(max_length=100 , blank=True , null=True)
    Sehit_Meslegi = models.CharField(max_length=100 , blank=True , null=True)
    Sehit_Dogum_Yili = models.IntegerField(null=True , blank=True)
    Sehit_Resmi = models.ImageField(upload_to='djangouploads/sehitler/images', blank=True , null=True)
    Sehit_Biyografi = models.TextField(null=True , blank=True)