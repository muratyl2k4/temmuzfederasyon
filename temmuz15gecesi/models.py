from django.db import models

class Temmuz15(models.Model):
    Image = models.ImageField(upload_to='temmuz15gecesi/static/img/')
    Title = models.CharField(max_length=200 , null=True , blank=True)
    Time = models.CharField(max_length=200 , null=True , blank=True)
    Description = models.TextField(null=True , blank=True)