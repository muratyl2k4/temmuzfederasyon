from django.db import models

class New(models.Model):
    Title = models.CharField(max_length=100 , blank=True , null=True)
    subTitle = models.CharField(max_length=100 , blank=True , null=True)
    Description = models.TextField(blank=True , null=True)
    image = models.ImageField(upload_to='djangouploads/news/images' , blank=True , null=True)

    def __str__(self) :
        return self.Title