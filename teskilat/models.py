from django.db import models

class Iller(models.Model):
    Sehir = models.CharField(max_length=200 ,blank=True , primary_key=True)
