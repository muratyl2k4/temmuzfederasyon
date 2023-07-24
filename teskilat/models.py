from django.db import models

class Il(models.Model):
    Sehir_Ismi = models.CharField(max_length=200 ,blank=True , primary_key=True)
    Sehir_Plaka_Kodu = models.IntegerField(null=True , blank=True)
    
    def __str__(self) :
        return self.Sehir_Ismi
class Ilce(models.Model):
    Ilce_Sehir = models.ForeignKey(Il , null=True , blank=True , on_delete=models.CASCADE)
    Ilce_Ismi = models.CharField(max_length=100) 
    def __str__(self) :
        return str(self.Ilce_Sehir) + '-' +  self.Ilce_Ismi

class Il_Baskanligi(models.Model):
    Yonetici_Il = models.ForeignKey(Il , null=True , blank=True , on_delete=models.CASCADE)
    Yonetici_Ismi = models.CharField(max_length=200 , null=True ,blank=True)
    Yonetici_Sifati = models.CharField(max_length=200, null=True ,blank=True )
    Yonetici_Biyografisi = models.TextField(null=True ,blank=True)
    Yonetici_Resmi = models.ImageField(upload_to='djangouploads/teskilat/il_baskanligi/')
    Yonetici_Durumu = models.CharField(max_length=50 ,choices=[('Baskan' , 'Baskan') , 
                                                               ('Diger' , 'Diger')] ,default='Diger' ,  null=True , blank=True)

    def __str__(self) :
        return self.Yonetici_Ismi
class Il_Genclik_Kollari(models.Model):
    Yonetici_Il = models.ForeignKey(Il , null=True , blank=True , on_delete=models.CASCADE)
    Yonetici_Ismi = models.CharField(max_length=200 , null=True ,blank=True)
    Yonetici_Sifati = models.CharField(max_length=200, null=True ,blank=True )
    Yonetici_Biyografisi = models.TextField(null=True ,blank=True)
    Yonetici_Resmi = models.ImageField(upload_to='djangouploads/teskilat/il_baskanligi/')
    Yonetici_Durumu = models.CharField(max_length=50 ,choices=[('Baskan' , 'Baskan') , 
                                                               ('Diger' , 'Diger')] ,default='Diger' ,  null=True , blank=True)

    def __str__(self) :
        return self.Yonetici_Ismi

class Il_Kadin_Kollari(models.Model):
    Yonetici_Il = models.ForeignKey(Il , null=True , blank=True , on_delete=models.CASCADE)
    Yonetici_Ismi = models.CharField(max_length=200 , null=True ,blank=True)
    Yonetici_Sifati = models.CharField(max_length=200, null=True ,blank=True )
    Yonetici_Biyografisi = models.TextField(null=True ,blank=True)
    Yonetici_Resmi = models.ImageField(upload_to='djangouploads/teskilat/il_baskanligi/')
    Yonetici_Durumu = models.CharField(max_length=50 ,choices=[('Baskan' , 'Baskan') , 
                                                               ('Diger' , 'Diger')] ,default='Diger' ,  null=True , blank=True)

    def __str__(self):
        return self.Yonetici_Ismi
class Ilce_Baskanligi(models.Model):
    Yonetici_Il = models.ForeignKey(Ilce , null=True , blank=True , on_delete=models.CASCADE)
    Yonetici_Ismi = models.CharField(max_length=200 , null=True ,blank=True)
    Yonetici_Sifati = models.CharField(max_length=200, null=True ,blank=True )
    Yonetici_Biyografisi = models.TextField(null=True ,blank=True)
    Yonetici_Resmi = models.ImageField(upload_to='djangouploads/teskilat/ilce_baskanligi/')
    Yonetici_Durumu = models.CharField(max_length=50 ,choices=[('Baskan' , 'Baskan') , 
                                                               ('Diger' , 'Diger')] ,default='Diger' ,  null=True , blank=True)
    def __str__(self):
            return self.Yonetici_Ismi
class Ilce_Genclik_Kollari(models.Model):
    Yonetici_Il = models.ForeignKey(Ilce , null=True , blank=True , on_delete=models.CASCADE)
    Yonetici_Ismi = models.CharField(max_length=200 , null=True ,blank=True)
    Yonetici_Sifati = models.CharField(max_length=200, null=True ,blank=True )
    Yonetici_Biyografisi = models.TextField(null=True ,blank=True)
    Yonetici_Resmi = models.ImageField(upload_to='djangouploads/teskilat/ilce_baskanligi/')
    Yonetici_Durumu = models.CharField(max_length=50 ,choices=[('Baskan' , 'Baskan') , 
                                                               ('Diger' , 'Diger')] ,default='Diger' ,  null=True , blank=True)
    def __str__(self):
            return self.Yonetici_Ismi
class Ilce_Kadin_Kollari(models.Model):
    Yonetici_Il = models.ForeignKey(Ilce , null=True , blank=True , on_delete=models.CASCADE)
    Yonetici_Ismi = models.CharField(max_length=200 , null=True ,blank=True)
    Yonetici_Sifati = models.CharField(max_length=200, null=True ,blank=True )
    Yonetici_Biyografisi = models.TextField(null=True ,blank=True)
    Yonetici_Resmi = models.ImageField(upload_to='djangouploads/teskilat/ilce_baskanligi/')
    Yonetici_Durumu = models.CharField(max_length=50 ,choices=[('Baskan' , 'Baskan') , 
                                                               ('Diger' , 'Diger')] ,default='Diger' ,  null=True , blank=True)
    def __str__(self):
            return self.Yonetici_Ismi