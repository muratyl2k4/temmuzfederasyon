from django.db import models

class Bagis(models.Model):
    Baslik = models.CharField(max_length=200 , null=True , blank=True)
    Tutar = models.IntegerField(null=True , blank=True)
    Aciklama= models.TextField(null=True , blank=True)