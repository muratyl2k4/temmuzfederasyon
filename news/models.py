from django.db import models

class New(models.Model):
    Title = models.CharField(max_length=100 , blank=True , null=True)
    subTitle = models.CharField(max_length=100 , blank=True , null=True)
    Description = models.TextField(blank=True , null=True)
    image = models.ImageField(upload_to='news/static/img/' , blank=True , null=True)